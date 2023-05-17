import unittest
from app import app

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_send_email(self):
        data = {
            'name': 'John',
            'surname': 'Doe',
            'phone': '1234567890',
            'email': 'john.doe@example.com',
            'topic': 'Test Topic',
            'text': 'Test Message'
        }

        response = self.app.post('/send_email', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Email sent successfully')

if __name__ == '__main__':
    unittest.main()