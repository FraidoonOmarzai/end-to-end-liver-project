from liver.constants import *
from liver.utils.common import read_yaml, create_directories
from liver.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    def __init__(self, config_file=CONFIG_FILE_PATH):
        self.config_path = read_yaml(config_file)

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
