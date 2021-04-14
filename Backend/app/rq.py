from celery import Celery
from time import sleep
from mail import Mail
from os import environ

# environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

# broker_url = "amqp://localhost"
# redis_url = "redis://localhost"
# broker_url = 'amqp://guest:guest@localhost:5672'
broker_url = "amqp://localhost"
redis_url = "redis://localhost"
broker_url = 'amqp://guest:guest@localhost:5672'

app = Celery('tasks', broker=redis_url, backend=redis_url)
# app.config_from_envvar('CELERY_CONFIG_MODULE')
# app = Celery('tasks', broker=broker_url, backend=redis_url)


@app.task
def say_hello(name: str):
    sleep(5)
    return f"Hello {name}"


def get_receiver_data():
    return {"mail": 'pawelm18@gmail.com', "time": '19:00', "topic": "Python"}

def get_tutor_data():
    return {"mail": 'pawel.matejko.printest@gmail.com', "first_name": 'Pawel', "last_name": "Matejko"}

def get_meeting_data():
    return {"date": '2021-04-13', "time": '19:00', "topic": "Python", "link": r"https://us05web.zoom.us/j/82250376345?pwd=bndiSEFZNFdTU0VKQ0tmYmw5bHBGUT09"}


@app.task
def send_mail(who_is_sending, who_is_reciving, when):
    # job_records = add_record(who_is_sending, who_is_reciving, when)
    # update_meeting_status("New")
    # receiver_data = get_receiver_data(who_is_sending)  # database
    # tutor_data = get_tutor_data(who_is_reciving)  # database
    # meeting_data = get_meeting_data(when)  # database
    # url, date, time = create_meeting("zoom")
    # update_meeting_status("created")
    # # check_if_tutor_is_avaiable() # database method
    receiver_data = get_receiver_data() #database
    tutor_data = get_tutor_data() # database
    meeting_data = get_meeting_data() # database
    print(receiver_data, tutor_data, meeting_data)
    mail = Mail(receiver_data, tutor_data, meeting_data)  # mail Class
    mail.create_message()
    mail.send_mail()
    # update_meeting_status("send")
    return "Complited!"
