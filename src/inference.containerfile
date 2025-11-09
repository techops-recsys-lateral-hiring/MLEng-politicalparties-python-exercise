FROM python:3.10
WORKDIR /app

COPY ./model_inference_endpoint/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./text_loader/ ./text_loader/
COPY ./model_inference_endpoint/ .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
