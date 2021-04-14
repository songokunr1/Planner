import smtplib, ssl
import credentials
from email.mime.text import MIMEText


message = f"""\
Subject: Hi there 

This message is sent from Python."""


class Mail:
    context = ssl.create_default_context()
    port = 465
    credentials = credentials.config['mail']
    # Create a secure SSL context

    def __init__(self, reciver_data, tutor_data, meeting_data):
        self.reciver_data = reciver_data
        self.tutor_data = tutor_data
        self.meeting_data = meeting_data
        self.msg = self.create_message()
    def send_mail(self):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.credentials['login'], self.credentials['password'])
            server.sendmail(self.credentials['login'], 'pawelm18@gmail.com', self.msg.as_string())

    def create_message(self):
        text_to_send = f"""
        Cześć, dziękuję za rezerwację spotkania! 
        Tutaj znajduje się link do spotkania: {self.meeting_data['link']}
        Gdybyś miał jakieś pytania to pisz na: {self.tutor_data['mail']}. \n
        Do zobaczenia. {self.tutor_data['first_name']} {self.tutor_data['last_name']}
        """
        self.msg = MIMEText(text_to_send)
        self.msg['Subject'] = f"{self.meeting_data['date']} {self.meeting_data['time']} - {self.meeting_data['topic']}"
        return self.msg


def get_reciver_data():
    return {"mail": 'pawelm18@gmail.com', "time": '19:00', "topic": "Python"}

def get_tutor_data():
    return {"mail": 'pawel.matejko.printest@gmail.com', "first_name": 'Pawel', "last_name": "Matejko"}

def get_meeting_data():
    return {"date": '2021-04-13', "time": '19:00', "topic": "Python", "link": r"https://us05web.zoom.us/j/82250376345?pwd=bndiSEFZNFdTU0VKQ0tmYmw5bHBGUT09"}




if __name__ == "__main__":
    reciver_data = get_reciver_data() #database
    tutor_data = get_tutor_data() # database
    meeting_data = get_meeting_data() # database
    # check_if_tutor_is_avaiable() # database method


    mail = Mail(reciver_data, tutor_data, meeting_data) # mail Class
    mail.create_message()
    mail.send_mail()
