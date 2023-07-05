```python
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_user_creation(self):
        self.assertIsInstance(self.user, User)
        self.assertEqual(self.user.__str__(), 'testuser')

    def test_user_authentication(self):
        logged_in = self.client.login(username='testuser', password='12345')
        self.assertTrue(logged_in)

    def test_user_logout(self):
        self.client.login(username='testuser', password='12345')
        self.client.logout()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
```