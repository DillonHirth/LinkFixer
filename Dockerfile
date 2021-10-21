# syntax=docker/dockerfile:1
FROM python:3.9-slim-buster AS base

# Setup env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

# Install pipenv
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile* .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy --ignore-pipfile

FROM base AS runtime

# Copy virtual env from python-deps stage
COPY --from=python-deps /.venv /.venv
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY . .
ENTRYPOINT ["python3", "bot_src/__main__.py"]