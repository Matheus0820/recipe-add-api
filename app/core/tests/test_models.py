"""
Test for models.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test models."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

        def test_new_user_email_normalized(self):
            """Test email is normalized for new users."""
            semple_emails = [
                ['test1@EXAMPLE.com', 'test1@exemple.com'],
                ['Test2@Exemple.com', 'Test2@exemple.com'],
                ['TEST3@EXEMPLE.com', 'TEST3@exemple.com'],
                ['test4@exemple.COM', 'test4@exemple.com'],
            ]
            for email, expected in sample_emails:
                user = get_user_model().objects.create_user(email, 'sample123')
                self.assertEqual(user.email, expected)

        def test_new_user_without_email_raises_error(self):
            """Test that creating a user without an email raises a ValueError."""
            with self.assertRaises(ValueError):
                get_user_model().objects.create_user('', 'test123')
