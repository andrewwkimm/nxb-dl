# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.187.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3.10"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

RUN \
    apt-get upgrade \
    && apt-get update \
    && apt-get install -y bash-completion curl \
    && apt install chromium chromium-driver -y \
    && pip install pre-commit

# Coding only for vscode user and not root
USER vscode

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && bash -c "echo 'source <(poetry completions bash)' >> ~/.bashrc"
