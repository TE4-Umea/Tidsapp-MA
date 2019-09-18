import unittest
import json
import flask

import util
from timer import app


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = util.get_env("token")

    def test_user_status(self):
        """
        This checks the users status.
        Expected outcome is a return status of 200 and a message saying:
        `Data successfully gathered. Toggle status is active / inactive.
         You have worked for x hours today, and y hours this week.
         You're currently working on project z and part of the team xyz.`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_status/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertTrue(len(rv.data) > 0)

    def test_badtoken_user_status(self):
        """
        This tries to check a users status with a bad token.
        Expected outcome is a return status of 200 and a error message saying.
        `Error has occurred, The specified token is invalid`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user_status/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified token is invalid")

