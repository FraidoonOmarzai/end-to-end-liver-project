from liver.constants import *
from liver.utils.common import read_yaml, create_directories
from liver.entity.config_entity import (DataIngestionConfig,
                                        DataValidationConfig,
                                        DataTransformationConfig,
                                        ModelTrainConfig)


class ConfigurationManager:
    def __init__(self,
                 config_file=CONFIG_FILE_PATH,
                 schema_file=SCHEMA_FILE_PATH,
                 params=PARAMS_FILE_PATH):
        self.config_path = read_yaml(config_file)
        self.schema = read_yaml(SCHEMA_FILE_PATH)
        self.params_path = read_yaml(PARAMS_FILE_PATH)

        create_directories([self.config_path.artifacts_root])

    def dataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config_path.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    def data_validation_config(self) -> DataValidationConfig:
        config = self.config_path.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])

        datavalidationconfig = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_dir=config.unzip_dir,
            status=config.status,
            all_schema=schema
        )

        return datavalidationconfig

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config_path.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            dataset=config.dataset
        )

        return data_transformation_config

    def get_model_train_config(self) -> ModelTrainConfig:
        config = self.config_path.model_training
        schema = self.schema
        params = self.params_path

        create_directories([config.root_dir])

        model_train_config = ModelTrainConfig(
            root_dir=config.root_dir,
            train_path=config.train_path,
            test_path=config.test_path,
            model_name=config.model_name,
            target=schema.TARGET.name,
            n_estimators=params.Random_forest.n_estimators,
            min_samples_split=params.Random_forest.min_samples_split,
            min_samples_leaf=params.Random_forest.min_samples_leaf,
            max_depth=params.Random_forest.max_depth
        )

        return model_train_config
