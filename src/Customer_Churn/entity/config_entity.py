from Customer_Churn.config.configuration import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from Customer_Churn.utils.common import read_yaml, create_directories
from Customer_Churn.constants import *

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH, 
                 params_filepath=PARAMS_FILE_PATH, 
                 schema_filepath=SCHEMA_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])
        
        schema = self.schema.COLUMNS
        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            unzip_dir = config.unzip_data_dir,
            STATUS_FILE = config.STATUS_FILE,
            all_schema = schema
        )
        return data_validation_config

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])
        
        data_tranformation_config = DataTransformationConfig(
            root_dir = config.root_dir,
            data_path = config.data_path
        )
        return data_tranformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        schema = self.schema.TARGET_COLUMN
        params = self.params.XGBoost

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            objective = params.objective,
            eval_metric = params.eval_metric,
            scale_pos_weight = params.scale_pos_weight,
            early_stopping_rounds = params.early_stopping_rounds,
            n_estimators = params.n_estimators,
            max_depth = params.max_depth,
            learning_rate = params.learning_rate,
            subsample = params.subsample,
            colsample_bytree = params.colsample_bytree,
            min_child_weight = params.min_child_weight,
            gamma = params.gamma,
            reg_alpha = params.reg_alpha,
            reg_lambda = params.reg_lambda,
            target_column = schema.name
        )
        return model_trainer_config
