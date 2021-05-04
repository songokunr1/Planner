FROM python:3.9-alpine
WORKDIR /mail
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . ./
RUN apk add make
RUN apk --update --no-cache add python3-dev libffi-dev gcc musl-dev make libevent-dev build-base
RUN pip install -r requirements.txt
RUN pip install celery
EXPOSE 8888
# CMD ["flask", "run"]