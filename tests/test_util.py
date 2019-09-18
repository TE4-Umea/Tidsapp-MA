from unittest import TestCase
import util


class TestUtil(TestCase):
    def test_get_token(self):
        """
        Test to check if it util file can load the variables in the env file.
        Prerequisites: In the env file Write "Token=ATestToken" followed by a new line.
        Expected outcome, Test passes.
        """
        token = util.get_env("token")
        self.assertTrue((len(token) > 0))
        self.assertEqual(token, "ATestToken")
