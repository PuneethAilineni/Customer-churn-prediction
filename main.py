from Customer_Churn import Logger
from Customer_Churn.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from Customer_Churn.pipeline.data_validation_pipeline import DataValidationTrainingPipeline
from Customer_Churn.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from Customer_Churn.pipeline.model_training_pipeline import ModelTrainingPipeline

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
    
stage_name = 'Data Transformation stage'

try:
    Logger.info(f">>> stage =>{stage_name} has started <<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    Logger.info(f">>> stage {stage_name} has ended <<<")
except Exception as e:
    Logger.info(e)
    raise e

stage_name = 'Model Training stage'

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = ModelTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e
