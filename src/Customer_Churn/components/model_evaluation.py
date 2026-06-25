import pandas as pd
from sklearn.metrics import classification_report
import mlflow
import mlflow.sklearn
import joblib
from pathlib import Path
from urllib.parse import urlparse
from Customer_Churn.entity.config_entity import ModelEvaluationConfig
from Customer_Churn.utils.common import save_json 

class ModelEvaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config

    def eval_metric(self, actual, pred):
        return classification_report(actual, pred, output_dict=True)
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis = 1).copy()
        test_y = test_data[[self.config.target_column]].copy()

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            report = self.eval_metric(test_y, predicted_qualities)

            overall_accuracy = report['accuracy']
            class_1_precision = report['1']['precision']
            class_1_recall    = report['1']['recall']
            class_1_f1_score  = report['1']['f1-score']
            class_0_recall    = report['0']['recall']

            print(f"accuracy = {overall_accuracy}, class 1 recall(minority class) = {class_1_recall}")
            save_json(path = Path(self.config.metric_file_name), data = report)

            mlflow.log_params(self.config.all_parms)

            mlflow.log_metric("Accuracy",overall_accuracy)
            mlflow.log_metric("class 1 precision",class_1_precision)
            mlflow.log_metric("class 1 recall",class_1_recall)
            mlflow.log_metric("class 1 f1 score",class_1_f1_score)

            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name = "XGBoost",
                                         skops_trusted_types=['xgboost.core.Booster', 'xgboost.sklearn.XGBClassifier'])
            else:
                mlflow.sklearn.load_model(model,"model",
                                          skops_trusted_types=['xgboost.core.Booster', 'xgboost.sklearn.XGBClassifier'])
