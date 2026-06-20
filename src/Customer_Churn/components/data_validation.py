import os
from Customer_Churn import Logger
from Customer_Churn.entity.config_entity import DataValidationConfig
import pandas as pd

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = True

            data = pd.read_csv(self.config.unzip_dir)
            data = data.drop("customer_id", axis = 1)
            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
            
            with open(self.config.STATUS_FILE,'w') as f:
                f.write(f"validation status => {validation_status}")
            Logger.info(f"validation status is => {validation_status}")
            return validation_status
        except Exception as e:
            print(e)
            raise e