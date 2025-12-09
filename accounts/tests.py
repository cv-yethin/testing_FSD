from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class AuthFlowTests(TestCase):
    def test_signup_login_logout_flow(self):
        resp = self.client.post(reverse("accounts:signup"), {
            "username": "alice",
            "email": "alice@example.com",
            "password1": "Astrongpass123",
            "password2": "Astrongpass123",
        })
        self.assertRedirects(resp, reverse("accounts:dashboard"))
        resp = self.client.get(reverse("accounts:dashboard"))
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get(reverse("accounts:logout"))
        self.assertRedirects(resp, reverse("accounts:login"))
        resp = self.client.get(reverse("accounts:dashboard"))
        self.assertRedirects(resp, f"{reverse('accounts:login')}?next={reverse('accounts:dashboard')}")

    def test_login_existing_user(self):
        User.objects.create_user(username="bob", password="AStrongpass123", email="bob@example.com")
        resp = self.client.post(reverse("accounts:login"), {
            "username": "bob",
            "password": "AStrongpass123",
        })
        self.assertRedirects(resp, reverse("accounts:dashboard"))