FROM python:3.10-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

EXPOSE 8000