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

12. **Flask App**
* add the required html and css to the project
* define app.py
* run the app

13. **Docker And GithubAction(CI/CD)**
* define the docker file
* bulid and run the docker image

```bash
docker build -t liver-app .  # build docker image
docker ps   
docker images
docker run -p 8080:8080 liver-app
```
**Note:** The app work well using docker in pc 

* login to docker hub and create a repository. (add DOCKERHUB_TOKEN and DOCKERHUB_USERNAME to github secrets)

* using github-action to push the docker image to docker hub
```bash
name: Docker Build and Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v1

    - name: Login to Docker Hub
      run: echo ${{ secrets.DOCKERHUB_TOKEN }} | docker login -u ${{ secrets.DOCKERHUB_USERNAME }} --password-stdin

    - name: Build and push
      run: |
        docker build -t fraidoonjan/pneumonia:v1 .
        docker push fraidoonjan/pneumonia:v1

```

### 14. **AWS**

* Deploy our docker image to AWS using Github-Actions
#### Setps:

1. Login to AWS console
2. Create IAM user for deployment and download the accessKeys

```bash
#with specific access

1. ECR: Elastic Container registry to save your docker image in aws
2. EC2 access : It is virtual machine


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy for IAM:

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess
```

3. Create ECR repo to store/save docker image
```bash
- Save the URI: 060145207853.dkr.ecr.eu-north-1.amazonaws.com/liver-project
```
4. Create EC2 machine (Ubuntu)
5. Open EC2 and Install docker in EC2 Machine:

```bash
#optinal

sudo apt-get update

sudo apt-get upgrade -y

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
```

6. Configure EC2 as self-hosted runner:
```bash
setting-->actions-->runner-->new self hosted runner--> choose os--> copy each command and run it on EC2 Instance Connect
```
7. Setup github secrets:
```bash
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = eu-north-1

AWS_ECR_LOGIN_URI =  060145207853.dkr.ecr.eu-north-1.amazonaws.com

ECR_REPOSITORY_NAME = liver-project
```
