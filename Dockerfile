FROM python:3.9.0-slim as build-image

WORKDIR /usr/local/bin/gig

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y curl ca-certificates gnupg
RUN curl https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get install -y gcc g++ make postgresql-server-dev-all libpq-dev libffi-dev git cargo

COPY ./ /tmp/build
COPY src/gig_python_test/db/migrations ./migrations/
COPY src/gig_python_test/db/alembic.ini ./alembic.ini

RUN  (cd /tmp/build \
     && python3 -m venv py3env-dev \
     && . py3env-dev/bin/activate \
     && python3 -m pip install -U -r requirements_dev.txt \
     && python3 setup.py bdist_wheel)


RUN  export APP_HOME=/usr/local/bin/gig \
     && (cd $APP_HOME \
         && python3 -m venv py3env \
         && . py3env/bin/activate \
         && python3 -m pip install -U pip \
         && python3 -m pip install -U setuptools \
         && python3 -m pip install -U wheel \
         && python3 -m pip install -U gig_python_test --find-links=/tmp/build/dist)


FROM python:3.9.0-slim

ENV  PYTHONPATH=/usr/local/bin/gig

RUN  mkdir -p /usr/local/bin/gig \
     && apt-get update \
     && apt-get -y upgrade \
     && apt-get install -y libpq-dev

WORKDIR /usr/local/bin/gig

COPY --from=build-image /usr/local/bin/gig/ ./

RUN  groupadd -r appgroup \
     && useradd -r -G appgroup -d /home/appuser appuser \
     && install -d -o appuser -g appgroup /usr/local/bin/gig/logs

USER  appuser

EXPOSE 8080


CMD ["/usr/local/bin/gig/py3env/bin/python3", "-m", "uvicorn", "gig_python_test.api.http:app", "--host", "0.0.0.0", \
     "--port", "8080"]

