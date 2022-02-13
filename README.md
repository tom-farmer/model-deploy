# Simple Containerized Model Deployment Stack

Goals for this project
 - Perform data exploration in a notebook
 - train a model and write out a model artifact
 - write a script to respond to a request with flask
 - deploy model using docker and request inference from docker container

 Data is in data/ directory that isn't included in the git repo.  The data can be found here: https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data

 Technologies used in this demo:
  - Local Jupyter Notebooks
  - Conda for package management
  - Python
    - Pandas for data manipulation
    - Scikit-Learn for modeling
    - joblib for object serialization
    - Flask for api
  - docker
  - git
