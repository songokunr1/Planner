from email.mime.text import MIMEText


class TeamsMailCreator:
    def __init__(self, recipient_data, tutor_data, meeting_data):
        self.recipient_data = recipient_data
        self.tutor_data = tutor_data
        self.meeting_data = meeting_data

        self.msg = self.create_message()

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

    @property
    def recipient(self):
        return self.recipient_data['mail']
