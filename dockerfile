FROM python:3.8

EXPOSE 5000

# Install miniconda
ENV CONDA_DIR /opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
     /bin/bash ~/miniconda.sh -b -p /opt/conda

# Put conda in path so we can use conda activate
ENV PATH=$CONDA_DIR/bin:$PATH

COPY requirements.txt /tmp/requirements.txt
RUN conda create --name deploy --file /tmp/requirements.txt
RUN conda activate deploy

COPY ./models /code/models
COPY ./python /code/python
COPY model_inference.py /code/model_inference.py

WORKDIR /code

RUN python3 model_inference.py
