import unittest
import json
import os
from timer import app


class TestManagerStatus(unittest.TestCase):
    def setUp(self):
        from dotenv import load_dotenv
        load_dotenv()
        self.app = app.test_client()
        self.token = os.getenv("token")

    def test_no_token(self):
        """
        Tests to make sure that the all paths return error if no token is present.
        :rtype: void
        """
        # Python dictionary
        payload = {
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFADSS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        }

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/status', query_string=payload)
        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data.decode(), "Error has occurred, The specified token is invalid")

    def test_manager_specified_status(self):
        """
        Show status of the specified user with post.
        Expected outcome: to print a list of users and time they have spent.
        :return:
        """
        # Python dictionary
        payload = {
            "user_name": "user.name",
            "user_id": "UMU0VNH09",
            "token": self.token,
            "text": "Test Testsson"
        }
        # Sends a POST request to get the "/manager_status/" endpoint
        maru = self.app.post('/manager/status', query_string=payload)

        # Makes sure that the response status is 200.
        assert maru.status == '200 OK'

        # Asserts that the response is the what to be expected.
        self.assertTrue(len(maru.data) > 0)

    def test_manager_status(self):
        """
        Show status of every user.
        Expected outcome: to print a list of users and time they have spent.
        :return:
        """
        # Python dictionary
        payload = {
            "user_name": "user.name",
            "user_id": "UMU0VNH09",
            "token": self.token,
            "text": ""
        }

        # Sends a POST request to get the "/manager_status/" endpoint
        maru = self.app.post('/manager/status', query_string=payload)

        # Makes sure that the response status is 200.
        assert maru.status == '200 OK'

        # Asserts that the response is the what to be expected.
        self.assertTrue(len(maru.data) > 0)

    def test_manager_move(self):
        """
        Moves users to a different team specified with post
        type the user name and then the name of the team.
        Expected outcome to move user to a new team.
        :return:
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "Smith new Team0"
        }
        # Sends a POST request to get the "/manager_move/" endpoint
        maru = self.app.post('/manager/move', query_string=payload)

        # Makes sure that the response status is 200.
        assert maru.status == '200 OK'

        # Asserts that the response is the what to be expected.
        self.assertTrue(len(maru.data) > 0)
        self.assertEqual(maru.data.decode(), "User Moved to a new team successfully")
