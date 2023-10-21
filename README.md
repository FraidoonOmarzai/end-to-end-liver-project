## Steps:

```bash
## Workflows
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py
```

1. Git clone the repository and Define template of the project

```bash
touch template.py
python3 template.py
```

2. define setup.py scripts (**The setup.py** is a module used to build and distribute Python packages. It typically contains information about the package)


3. Create environment and install dependencies

```bash
conda create -n liver-env python=3.10 -y
conda activate mlops-env
pip install -r requirements.txt
```

4. define logger (**The Logging** is a means of tracking events that happen when some software runs)

5. define utils (**The utils.py** makes it easy to execute common tasks in Python scripts)

6. **Data Ingestion**

* define config/config.yaml and constant.yaml --> add 01_data_ingestion.ipynb  
* entity --> configuration manager --> componenets --> pipeline and finally run stage_01_data_ingestion.py

7. **EDA**

* load the dataset
* statistical checking
* checking number of unique values for each columns
* check data type
* check duplicate values
* check null values
* check balance of the dataset
* check outliers
* visualization
* checking correlation


8. **dvc**

* define dvc.yaml

```bash
dvc init
dvc repro
dvc dag
```

9. **Data Validation**

* define config.yaml and schema.yaml --> 02_data_validation.ipynb
* entity --> configuration manager --> componenets --> pipeline stage_02_data_validation.py --> run dvc


10. **Data Transformation**

* define config.yaml --> 03_data_transformation.ipynb (drop null values, label encoding, handle imbalance datasets, train test split)
* entity --> configuration manager --> componenets --> pipeline stage_03_data_transformation.py --> run dvc


11. **Model Training**

* define config.yaml and params.yaml --> 04_model_training.ipynb
* entity --> configuration manager --> componenets --> pipeline stage_04_model_training.py --> run dvc

12. **Model Evaluation**

* define config.yaml and schema.yaml--> 05_model_evaluation.ipynb

* Using MLflow 

* Setup dagshub, connect the github repos
```bash
MLFLOW_TRACKING_URI=https://dagshub.com/fraidoon_omarzai/end-to-end-liver-project.mlflow \
MLFLOW_TRACKING_USERNAME=fraidoon_omarzai \
MLFLOW_TRACKING_PASSWORD=bc25b16bd5206328d8899cf34377f26ad71d1420 \
python script.py
```

* Run this to export as env variables
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/fraidoon_omarzai/end-to-end-liver-project.mlflow
export MLFLOW_TRACKING_USERNAME=fraidoon_omarzai 
export MLFLOW_TRACKING_PASSWORD=bc25b16bd5206328d8899cf34377f26ad71d1420
```

* entity --> configuration manager --> componenets --> pipeline stage_05_model_evaluation.py --> run dvc