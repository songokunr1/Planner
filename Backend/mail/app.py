from flask import Flask, request

from mail.creator.form import FormData, FormMailCreator
from mail.sender import Mailer

app = Flask(__name__)

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    surname = request.form['surname']
    phone = request.form['phone']
    email = request.form['email']
    topic = request.form['topic']
    text = request.form['text']

    form_data = FormData(name=name, surname=surname, phone=phone, email=email, topic=topic, text=text)

    mailer = Mailer()
    mailer_creator = FormMailCreator({'mail': ''}, form_data)
    mailer.send_mail(mailer_creator.recipient, mailer_creator.msg)

    return 'Email sent successfully'

if __name__ == '__main__':
    app.run(port=8888)
