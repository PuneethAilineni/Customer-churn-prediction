from Customer_Churn import Logger
from Customer_Churn.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from Customer_Churn.pipeline.data_validation_pipeline import DataValidationTrainingPipeline

stage_name = 'Data Ingestion stage'

try:
    Logger.info(f">>> stage =>{stage_name} has started <<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    Logger.info(f">>> stage {stage_name} has ended <<<")
except Exception as e:
    Logger.info(e)
    raise e

stage_name = 'Data Validation stage'

try:
    Logger.info(f">>> stage =>{stage_name} has started <<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    Logger.info(f">>> stage {stage_name} has ended <<<")
except Exception as e:
    Logger.info(e)
    raise e
    
