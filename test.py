from django.contrib.auth import get_user_model
from django.test import TestCase

User = get_user_model()

class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'test user',
            'email': 'testuser@example.com',
            'first_name' :'test',
			'last_name': 'user',
            'is_vendor': True,
            'is_customer': True,
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        # print(response.context)
        print(self.assertTrue(response.context['user'].is_active))