# syntax=docker/dockerfile:1
FROM python:3.11-buster AS base

# Setup env
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV PYTHONPATH=.

# Install pipenv
RUN pip install pipenv

# Install python dependencies in /.venv
COPY Pipfile* .
RUN pipenv install --system --deploy --ignore-pipfile

FROM base AS runtime

# Copy virtual env from python-deps stage
ENV PATH="/.venv/bin:$PATH"

# Install application into container
COPY . .
ENTRYPOINT ["python3", "link_fixer/__main__.py"]