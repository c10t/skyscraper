FROM python:3.6

WORKDIR /home/engine

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pip install pipenv \
 && pipenv install --system

EXPOSE 8000
ENTRYPOINT ["python"]
CMD ["-m",  "http.server", "8000"]
