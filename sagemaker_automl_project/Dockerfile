# Base stage with common dependencies
FROM python:3.9-slim as base
WORKDIR /app
COPY requirements.common.txt .
RUN pip install -r requirements.common.txt

# Development stage
FROM base as development
COPY requirements.dev.txt .
RUN pip install -r requirements.dev.txt

# Production stage
FROM base as production
COPY requirements.prod.txt .
RUN pip install -r requirements.prod.txt

COPY . .

CMD ["python", "main.py"]