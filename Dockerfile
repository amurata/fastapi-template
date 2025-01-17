FROM python:3.10-buster

ENV LANG C.UTF-8
ENV TZ UTC
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /backend/app:/backend
ENV TERM xterm-256color

RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libmariadb-dev \
    curl

# installing using version 1.4.2 - this will work
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python3 - --version 1.4.2 && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
RUN poetry install --verbose

#RUN bash -c "if [ $EVN == 'production' ]; then copy . ./backend; fi"
WORKDIR /backend
COPY ./pyproject.toml ./poetry.lock /backend/


# RUN poetry install --no-root
# poe scriptsのcompletionを設定
RUN poe _bash_completion >> /root/.bashrc
