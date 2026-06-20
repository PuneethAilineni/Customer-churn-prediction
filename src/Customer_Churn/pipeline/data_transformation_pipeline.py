from Customer_Churn.entity.config_entity import ConfigurationManager
from Customer_Churn.components.data_transformation import DataTransformation
from Customer_Churn import Logger

stage_name = 'Data Validation stage'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.transform()

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e