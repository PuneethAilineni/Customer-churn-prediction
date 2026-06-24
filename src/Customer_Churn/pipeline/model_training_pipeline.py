from Customer_Churn.entity.config_entity import ConfigurationManager
from Customer_Churn.components.model_training import ModelTrainer
from Customer_Churn import Logger

stage_name = 'Model Training stage'

class ModelTrainingPipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainser_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(model_trainser_config)
        model_trainer.train()

if __name__ == '__main__':
    try:
        Logger.info(f">>> stage =>{stage_name} has started <<<")
        obj = ModelTrainingPipeline()
        obj.main()
        Logger.info(f">>> stage {stage_name} has ended <<<")
    except Exception as e:
        Logger.info(e)
        raise e

