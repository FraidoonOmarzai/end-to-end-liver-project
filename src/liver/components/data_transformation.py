from liver import logger
import pandas as pd
from imblearn.over_sampling import RandomOverSampler
from collections import Counter
from sklearn.model_selection import train_test_split
import os
from liver.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self,
                 config: DataTransformationConfig) -> None:
        self.config = config

    def cleaning(self) -> pd.DataFrame:
        df = pd.read_csv(self.config.dataset)
        # print(df.head())
        # print(df.isnull().sum())
        df = df.dropna()  # drop null values
        # print(df.isnull().sum())
        logger.info(f"Null values removed: {df.isnull().sum()}")

        df.replace(to_replace={'Female': 0, 'Male': 1},
                   inplace=True)  # label encoding
        logger.info("labeled gander columns")

        return df

    def handle_imbalanced(self, df):
        X = df.drop(['Dataset'], axis=1)
        y = df['Dataset']

        logger.info('Original dataset shape %s' % Counter(y))

        os = RandomOverSampler()
        X, y = os.fit_resample(X, y)

        logger.info('Resampled dataset shape %s' % Counter(y))
        df = X
        df['Dataset'] = y

        return df

    def train_test_splits(self, df):
        train, test = train_test_split(df)
        train.to_csv(os.path.join(
            self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, "test.csv"), index=False)
        logger.info("Splited data into training and test sets")
        logger.info(f'train shape: {train.shape}')
        logger.info(f'test shape: {test.shape}')
