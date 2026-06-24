import os
import numpy as np
import pandas as pd
import xgboost as xgb
from Customer_Churn.entity.config_entity import ModelTrainerConfig 
import joblib

class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)     

        train_x = train_data.drop([self.config.target_column], axis = 1)
        test_x = test_data.drop([self.config.target_column], axis = 1)

        train_y = train_data[self.config.target_column].copy()
        test_y = test_data[self.config.target_column].copy()

        model = xgb.XGBClassifier(
            objective = self.config.objective, 
            eval_metric = self.config.eval_metric,
            scale_pos_weight = self.config.scale_pos_weight,
            # early_stopping_rounds = self.config.early_stopping_rounds,
            n_estimators=self.config.n_estimators,
            max_depth = self.config.max_depth,
            learning_rate = self.config.learning_rate,
            subsample = self.config.subsample,
            colsample_bytree = self.config.colsample_bytree,
            min_child_weight = self.config.min_child_weight,
            gamma = self.config.gamma,
            reg_alpha = self.config.reg_alpha,
            reg_lambda = self.config.reg_lambda,
        )

        model.fit(
            train_x,
            train_y
        )

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
