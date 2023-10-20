from liver.config.configuration import ConfigurationManager
from liver.components.data_transformation import DataTransformation
from liver import logger


STAGE_NAME = 'Data Transformation'


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(
            config=data_transformation_config)
        data = data_transformation.cleaning()
        data = data_transformation.handle_imbalanced(df=data)
        data_transformation.train_test_splits(df=data)


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
