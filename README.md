#Simple Containerized Model Deployment Stack

##Goals for this project
 - Perform data exploration in a notebook
 - train a model and write out a serialized model artifact
 - write a script to respond to an inference request with flask using the serialized model
 - Deploy model using docker and request inference from docker container

 Data is in data/ directory that isn't included in the git repo.  The data can be found here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

##Technologies used in this demo:
  - Local Jupyter Notebooks
  - Conda for package management
  - Python
    - Pandas for data manipulation
    - Scikit-Learn for modeling
    - joblib for object serialization
    - Flask for api
  - docker
  - git

##To Do:
 - Make training a python script
 - Make inference test use the test data

##Key Commands:
 - Build docker image:
  - `docker build https://github.com/tom-farmer/model-deploy.git#main`

## Resources:
 - https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#building-identical-conda-environments
