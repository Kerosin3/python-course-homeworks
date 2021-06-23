FROM python:3.9-buster

WORKDIR /app
ENV PYTHONPATH="${PYTHONPATH}:./"
RUN pip install -U pip
RUN pip install -U setuptools wheel
RUN pip install poetry
#RUN poetry config virtualenv.create false
RUN poetry config virtualenvs.create false --local

COPY ./pyproject.toml ./
COPY ./poetry.lock ./

RUN poetry install --no-interaction --no-ansi
#copy all
COPY . .

EXPOSE 5000

#ENV FLASK_ENV=development

RUN chmod +x entrypoint.sh
RUN chmod +x initialize.sh
ENTRYPOINT ["./entrypoint.sh"]
#CMD ["flask","run"]
CMD ["./initialize.sh","-dev"]
#CMD []
