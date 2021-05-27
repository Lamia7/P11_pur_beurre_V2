# from django.contrib.auth.models import AnonymousUser
# from django.contrib.auth.views import PasswordResetConfirmView
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse

from users.models import User


class TestUsersViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="user1",
            email="user1@gmail.com",
            password="password1234",
        )
        self.account_url = reverse("account")
        self.register_url = reverse("register")
        self.password_reset_url = reverse("password_reset")
        self.password_reset_done_url = reverse("password_reset_done")
        # self.password_reset_confirm_url = reverse("password_reset_confirm")
        # self.password_reset_complete_url = reverse("password_reset_complete")

    def test_registration_success(self):
        data = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password1": "password1234",
            "password2": "password1234",
        }

        self.client.post(self.register_url, data)
        self.assertEqual(User.objects.count(), 1)
        self.client.force_login(self.user)

    def test_account_page(self):
        # check that reverse the account template
        self.client.force_login(self.user)
        response = self.client.get(self.account_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account.html")

    def test_password_reset_page(self):
        # check that reverse the password_reset template
        response = self.client.get(self.password_reset_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset.html")

    def test_password_reset_done_page(self):
        response = self.client.get(self.password_reset_done_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "password_reset_done.html")
