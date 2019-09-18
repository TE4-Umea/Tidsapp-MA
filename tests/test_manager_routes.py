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
            "text": "user.name"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to get the "/manager_status/" endpoint
        maru = self.app.post('/manager/status', json=json_obj)

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
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to get the "/manager_status/" endpoint
        maru = self.app.post('/manager/status', json=json_obj)

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
            "text": "userName newTeam"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to get the "/manager_move/" endpoint
        maru = self.app.post('/manager/move', json=json_obj)

        # Makes sure that the response status is 200.
        assert maru.status == '200 OK'

        # Asserts that the response is the what to be expected.
        self.assertTrue(len(maru.data) > 0)
        self.assertEqual(maru.data, "Moving userName to teamName")
