FROM python:3.9-alpine
WORKDIR /planner
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
RUN apk add --no-cache gcc musl-dev linux-headers
COPY . /planner
COPY ./requirements.txt /planner/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask", "run"]