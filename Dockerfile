FROM python:3.11.2-alpine

ENV PYTHONBUFFERED 1

RUN pip install --upgrade pip

RUN adduser -D worker
USER worker
WORKDIR /home/worker

ENV PATH="/home/worker/.local/bin:${PATH}"

COPY --chown=worker:worker requirements.txt requirements.txt
RUN pip install --user -r requirements.txt


COPY --chown=worker:worker src .

LABEL mantainer="Brian Gratton <brian@gratton.us>" version="0.0.1"
