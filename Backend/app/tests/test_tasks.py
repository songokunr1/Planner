from ..rq import send_mail
from time import sleep
def test_mail():
    b = send_mail.delay(1,2,3)
    print(b.status)
    sleep(4)
    print(b.status)