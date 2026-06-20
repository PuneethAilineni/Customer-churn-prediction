import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from Customer_Churn.config.configuration import DataTransformationConfig
class DataTransformation:
    def __init__(self, config:DataTransformationConfig):
        self.config = config

    def feature_engineering(self, data) -> pd:
        data["balance_salary_ratio"] = (data["balance"] / (data["estimated_salary"] + 1))
        data["is_senior"] = (data["age"] > 60).astype(int)
        return data 

    def feature_selection(self, data) -> pd:
        data = data.drop(["customer_id", "age", "balance", "estimated_salary"], axis = 1)
        return data

    def transform(self):
        data = pd.read_csv(self.config.data_path)

        # featuer engineering
        data = self.feature_engineering(data)

        # feature selection
        data = self.feature_selection(data)

        # train test split
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

        print(train.shape)
        print(test.shape)
