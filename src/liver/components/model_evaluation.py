from liver import logger
from sklearn.metrics import f1_score, precision_score, recall_score
import pandas as pd
import joblib
from urllib.parse import urlparse
import mlflow
from liver.entity.config_entity import ModelEvaluationConfig
from liver.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, y_true, y_pred):
        f1 = f1_score(y_true, y_pred)
        precision = precision_score(y_true, y_pred)
        recall = recall_score(y_true, y_pred)

        return f1, precision, recall

    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_path)
        model = joblib.load(self.config.model_path)
        logger.info(self.config.mlflow_uri)
        test_x = test_data.drop([self.config.target], axis=1)
        test_y = test_data[[self.config.target]]

        mlflow.set_experiment(self.config.experiment_name)
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            pred = model.predict(test_x)

            (f1, precision, recall) = self.eval_metrics(test_y, pred)

            # Saving metrics as local
            scores = {"f1": f1, "precision": precision, "recall": recall}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("f1", f1)
            mlflow.log_metric("precision", precision)
            mlflow.log_metric("recall", recall)

            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                # Register the model
                # There are other ways to use the Model Registry, which depends on the use case,
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                mlflow.sklearn.log_model(
                    model, "model", registered_model_name="RandomForest")
            else:
                mlflow.sklearn.log_model(model, "model")
