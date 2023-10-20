from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    unzip_dir: Path
    status: str
    all_schema: dict
    
    
@dataclass
class DataTransformationConfig:
    root_dir: Path
    dataset: Path
    
    
@dataclass
class ModelTrainConfig:
    root_dir: Path
    train_path: Path
    test_path: Path
    model_name: str
    target: str
    n_estimators: float
    min_samples_split: float
    min_samples_leaf: float
    max_depth: float
