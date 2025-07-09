#
FROM python:3.11

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --upgrade setuptools wheel

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./app /code/app
WORKDIR /code/app

ENV PYTHONPATH="${PYTHONPATH}:/code"
#
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]