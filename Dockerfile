FROM python:3.7

ADD Stat_Calculator

RUN pip install --upgrade pop

CMD [ "python", "-m", ""]