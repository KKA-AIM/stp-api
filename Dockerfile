FROM cadquery/cadquery:latest

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn python-multipart

EXPOSE 8000

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]