# init a base image
FROM python:3.11.0a3-alpine3.15
# RUN apk add python3-dev \
#     && pip3 install --upgrade pip
# Define the present working directory
WORKDIR /my-short-url-app
# Copy the content into working directory
ADD . /my-short-url-app
# run pip to install the dependencies of the flask app
RUN pip3 install -r  requirements.txt
# Define the command to start the container
CMD ["python", "app.py"]