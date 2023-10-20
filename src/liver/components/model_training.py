from liver import logger
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import os
from liver.entity.config_entity import ModelTrainConfig


class ModelTraining:
    def __init__(self,
                 config: ModelTrainConfig) -> None:
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_path)
        test_data = pd.read_csv(self.config.test_path)

        X_train = train_data.drop([self.config.target], axis=1)
        y_train = train_data[[self.config.target]]

        model = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            min_samples_split=self.config.min_samples_split,
            min_samples_leaf=self.config.min_samples_leaf,
            max_depth=self.config.max_depth
        )

        model.fit(X_train, y_train)

        logger.info(f'Train model score: {model.score(X_train, y_train)}')

        joblib.dump(model, os.path.join(
            self.config.root_dir, self.config.model_name))
