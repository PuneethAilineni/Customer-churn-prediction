from Customer_Churn import Logger
from Customer_Churn.pipeline.data_ingestion_pipeline_01 import DataIngestionTrainingPipeline

stage_name = 'Data Ingestion stage'

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e