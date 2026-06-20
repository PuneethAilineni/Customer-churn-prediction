from Customer_Churn.entity.config_entity import ConfigurationManager
from Customer_Churn.components.data_validation import DataValidation
from Customer_Churn import Logger

stage_name = 'Data Validation stage'


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config = data_validation_config)
        data_validation.validate_all_columns()

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e