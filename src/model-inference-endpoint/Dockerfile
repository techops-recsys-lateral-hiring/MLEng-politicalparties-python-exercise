FROM python:3.9

WORKDIR /usr/src/app

COPY ./model-inference-endpoint/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY ./text_loader/ ./text_loader/
COPY ./model-inference-endpoint/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
