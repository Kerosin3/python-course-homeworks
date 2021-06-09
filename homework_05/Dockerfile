FROM python:3.9.5-buster

WORKDIR /app

RUN  pip install -U pip setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./web_app .
COPY info.sh .

ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

CMD ["echo","========!!!!!!!!!!!!!!!!!!!!!!!!============"]

RUN chmod +x info.sh

ENTRYPOINT ["./info.sh" ]
CMD ["flask","run","--host=0.0.0.0"]
