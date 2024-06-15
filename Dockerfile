# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create and set the working directory
RUN mkdir -p /code
WORKDIR /code

# Install dependencies
COPY requirements.txt /tmp/requirements.txt

RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

# Copy the local project
COPY . /code/

# Set the port number as an environment variable
ARG PORT=8000
ENV PORT $PORT

# Expose the given port
EXPOSE $PORT

# Use gunicorn to serve the application
CMD gunicorn --bind 0.0.0.0:$PORT --workers 2 django_project.wsgi
