
# Note: alpine python docker image throws gcc errors while attempting to install the package pycares, which this
# repo in its original form is reliant on.  Workarounds are encouraged and I would love to take a pull request from someone
# who can get the package built from an alpine image as the build time is much better and image size smaller.

FROM python:3.6.7

ENV PROJECT_HOME /chatterbox
ENV PROJECT_EXE /chatterbox/main.py
ENV PROJECT_README /chatterbox/README.md

ENV PROJECT_REQUIREMENTS /chatterbox/requirements.txt
ENV PROJECT_SRC /chatterbox/src

RUN mkdir $PROJECT_HOME

COPY src $PROJECT_SRC
COPY main.py $PROJECT_EXE
COPY README.md $PROJECT_README
COPY requirements.txt $PROJECT_REQUIREMENTS

RUN pip install -r $PROJECT_REQUIREMENTS

RUN chmod 755 $PROJECT_EXE

CMD python $PROJECT_EXE