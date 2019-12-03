FROM python:3.7.5-slim-buster

# Run this before dealing with our own virtualenv. The AWS CLI uses its own virtual environment
RUN pip3 install awscli

WORKDIR /app
ENV VENV /app/venv
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONPATH /app

# Set up a virtual environment to use with our workflows
RUN python3.7 -m venv ${VENV}
RUN ${VENV}/bin/pip install wheel

COPY dist/. /plugin/.
RUN ${VENV}/bin/pip install /plugin/flyteexampleplugin-0.0.1.tar.gz

# This is a script that enables a virtualenv, copy it to a better location
RUN cp ${VENV}/bin/flytekit_venv /opt/

# Copy the rest of the code
COPY demo/ .

# Set this environment variable. It will be used by the flytekit SDK during the registration/compilation steps
ARG DOCKER_IMAGE
ENV FLYTE_INTERNAL_IMAGE "$DOCKER_IMAGE"

# Enable the virtualenv for this image. Note this relies on the VENV variable we've set in this image.
ENTRYPOINT ["/opt/flytekit_venv"]
