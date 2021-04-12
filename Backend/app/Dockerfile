FROM python:3.9-alpine
WORKDIR /planner
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . /planner
RUN apk add make
RUN apk --update --no-cache add python3-dev libffi-dev gcc musl-dev make libevent-dev build-base
COPY ./requirements.txt /planner/requirements.txt
RUN pip install -r requirements.txt
RUN pip install celery
EXPOSE 5000
CMD ["flask", "run"]