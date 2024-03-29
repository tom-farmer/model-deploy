# Simple Containerized Model Deployment Stack

## Goals for this project
 - Perform data exploration in a notebook
 - train a model and write out a serialized model artifact
 - write a script to respond to an inference request with flask/gunicorn using the serialized model
 - Deploy model using docker and request inference from docker container
 - Push the container to AWS

 Data is in data/ directory that isn't included in the git repo.  The data can be found here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

## Technologies used in this demo:
  - Local Jupyter Notebooks
  - Conda for package management
  - Python 3.8
    - Pandas for data manipulation
    - Scikit-Learn for modeling
    - joblib for object serialization
    - Flask/gunicorn for rest api
  - docker
  - git
  - AWS
    - ECR: registered container to [public repository](https://gallery.ecr.aws/h8j7v9c1/tomfarmer)

## To Do:
 - Make training a python script
 - Make inference test use the test data

## Key Commands:
 - build image from git:
   - `docker build https://github.com/tom-farmer/model-deploy.git#main`
 - build image from local:
   - `docker build -t python/model_deploy:1.0 .`
 - run image first time:
   - docker run -d -P python/model_deploy:2.0
   - this does something weird with the ports, may need to specify them explicitly

## Resources:
 - https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments
