from liver.config.configuration import ConfigurationManager
from liver.components.data_validation import DataValidation
from liver import logger


STAGE_NAME = 'Data Validation'


class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        datavalidationconfig = config.data_validation_config()
        data_validation = DataValidation(config=datavalidationconfig)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
