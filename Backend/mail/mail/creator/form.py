from dataclasses import dataclass
from email.mime.text import MIMEText


@dataclass
class FormData:
    name: str
    surname: str
    phone: str
    email: str
    topic: str
    text: str


class FormMailCreator:
    def __init__(self, recipient_data, form_data: FormData):
        self.form_data = form_data
        self.recipient_data = recipient_data
        self.msg = self.create_mail()

    def create_mail(self):
        with open('form_template.html') as file:
            value = file.read()

        value = self.replace_form_values(value, self.form_data)
        self.msg = MIMEText(value, 'html')
        self.msg['Subject'] = f"{self.form_data.topic} {self.form_data.name} {self.form_data.surname}"
        return self.msg

    @property
    def recipient(self):
        return self.recipient_data['mail']


    def replace_form_values(self, html_value: str, form_data: FormData) -> str:
        for field_name, field_value in form_data.__dict__.items():
            placeholder = "{" + field_name.capitalize() + "}"
            html_value = html_value.replace(placeholder, str(field_value))
        return html_value
