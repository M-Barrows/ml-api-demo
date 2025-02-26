# Dockerfile.dash
# This is the file for building the Docker image

# Use the official Python image as the base image
FROM python:3.10.13-slim-bullseye

# Install UV
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Copy all code files into container
COPY . /app
# Install Dependencies
RUN uv sync --frozen --no-dev

ENV PATH="/app/.venv/bin:$PATH"

# Copy the rest of the code into the image
EXPOSE 8000
CMD ["uvicorn", "--host=0.0.0.0","run:app"]