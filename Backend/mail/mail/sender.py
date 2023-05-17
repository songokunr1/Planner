import smtplib, ssl
from mail import credentials
from email.mime.text import MIMEText

from mail.creator.form import FormData, FormMailCreator


class Mailer:
    context = ssl.create_default_context()
    port = 465
    credentials = credentials.config['mail']

    # Create a secure SSL context
    def send_mail(self, recipient, msg: MIMEText):
        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.credentials['login'], self.credentials['password'])
            server.sendmail(self.credentials['login'], recipient, msg.as_string())


if __name__ == "__main__":
    def get_reciver_data():
        return {"mail": 'pawelm18@gmail.com', "time": '19:00', "topic": "Python"}


    def get_tutor_data():
        return {"mail": 'pawel.matejko.printest@gmail.com', "first_name": 'Pawel', "last_name": "Matejko"}


    def get_meeting_data():
        return {"date": '2021-04-13', "time": '19:00', "topic": "Python",
                "link": r"https://us05web.zoom.us/j/82250376345?pwd=bndiSEFZNFdTU0VKQ0tmYmw5bHBGUT09"}

    reciver_data = get_reciver_data()  # database
    tutor_data = get_tutor_data()  # database
    meeting_data = get_meeting_data()  # database
    # check_if_tutor_is_avaiable() # database method

    mailer = Mailer()  # mail Class
    # mailer_creator = TeamsMailCreator(reciver_data, tutor_data, meeting_data)
    form_data = FormData(
            'Tester',
            'Kowalski',
    '444555555',
    'aaa@gmail.com',
    'Konsultacje',
    """czesc pisze zeby zobaczyc czy jestes w stanie mi pomoc he updated code includes a 
    <style> section where CSS rules are defined for the table, header cells (th),
    and data cells (td). It sets border-collapse to collapse, adds padding and alignment for cells, and applies a background color to the header row.  The border-bottom property adds a thin line below each row for separation."""
    )
    mailer_creator = FormMailCreator(reciver_data, form_data)
    mailer.send_mail(mailer_creator.recipient, mailer_creator.msg)
