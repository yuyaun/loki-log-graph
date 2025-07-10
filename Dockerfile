FROM python:3.11-slim
WORKDIR /app
COPY log_generator.py .
CMD ["python", "log_generator.py"]
