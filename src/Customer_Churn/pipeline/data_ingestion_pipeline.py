from Customer_Churn.entity.config_entity import ConfigurationManager
from Customer_Churn.components.data_ingestion import DataIngestion
from Customer_Churn import Logger

stage_name = 'Data Ingestion stage'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e