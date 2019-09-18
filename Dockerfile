FROM python:3.6-alpine

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

RUN chmod 766 $PROJECT_EXE

EXPOSE 5000

ENTRYPOINT ["usr/bin/python", '$PROJECT_EXE']