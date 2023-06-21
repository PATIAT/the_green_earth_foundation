from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


# Create your tests here.
class TestUserProfilesViews(TestCase):

    def test_404_error_if_no_profile_exists(self):
        response = self.client.get('profile')
        self.assertEqual(response.status_code, 404)

    def test_logged_in_user_can_access_profile(self):
        login = self.client.login(
            username='test_admin',
            password='sdf2398vsfhisdiofw9'
        )
        response = self.client.get(reverse('profile'))


class TestUserProfilesModels(TestCase):

    def test_string_representation(self):
        user = User(username="username_test")
        self.assertEqual(str(user), user.username)
