from liver.config.configuration import ConfigurationManager
from liver.components.model_training import ModelTraining
from liver import logger


STAGE_NAME = 'Model Training'


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        model_train_config = config.get_model_train_config()
        model = ModelTraining(model_train_config)
        model.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
