FROM python:3.8

EXPOSE 5000

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY ./models /code/models
COPY model_inference.py /code/model_inference.py

WORKDIR /code

CMD python3 model_inference.py
