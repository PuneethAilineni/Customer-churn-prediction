import os
from Customer_Churn.entity.config_entity import ConfigurationManager
from Customer_Churn.components.model_evaluation import ModelEvaluation
from Customer_Churn import Logger

stage_name = 'Model Evaluation stage'


class ModelEvaluationPipeline():
    def __init__(self):
        pass

    def main(self):
        os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/PuneethAilineni/Customer-churn-prediction.mlflow'
        os.environ['MLFLOW_TRACKING_USERNAME'] = 'PuneethAilineni'
        os.environ['MLFLOW_TRACKING_PASSWORD'] = '3f8d46a82c6f371481801e033eebeaf16d7bd193'
        
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(model_evaluation_config)
        model_evaluation.log_into_mlflow()

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e

