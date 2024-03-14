FROM python:3.11-slim
WORKDIR /api

# Environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_HOME="/opt/poetry"

# Install dependencies
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        gcc \
        build-essential \
        curl \
        libpq-dev \
        python3-dev \
    ; \
    rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN python -m pip install --no-cache-dir pipx
ENV PATH="/root/.local/bin:$PATH"
RUN pipx install poetry

# Pre-Copy
COPY ./pyproject.toml ./
RUN poetry config virtualenvs.create false
RUN poetry install --no-root --only main

# Copy
COPY . .

EXPOSE 8000

ENTRYPOINT ["bash", "./scripts/entrypoint.sh"]