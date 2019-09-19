import unittest
import json
import os
from timer import app


class TestCreateTeam(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app = app.test_client()
        self.token = os.getenv("token")

    def test_create_team(self):
        """
        This tries to create a team.
        The expected outcome is the return statement '200 OK'
        And the message 'Created team successfully' or
        'Error has occurred, Something went wrong'
        """
        # This parses dictionary to a json.
        json_obj = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "UMU0VNH09",
            "user_name": "elias.renman",
            "command": "/erdemo",
            "text": "new Team0212",
            "response_url": "https://hooks.slack.com/commands/TM1TFDZH8/748738219890/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })

        # Sends a POSt request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/team/create', json=json_obj)

        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data.decode(), "Created team successfully")

    def test_delete_non_existent_team(self):
        """
        This tries to delete a non existent team.
        The expected outcome is the return statement '200 OK'
        And an error message
        'Error has occurred, The specified team does not exist'
        """

        # Python dictionary
        json_obj = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "UMU0VNH09",
            "user_name": "elias.renman",
            "command": "/erdemo",
            "text": "delete team01",
            "response_url": "https://hooks.slack.com/commands/TM1TFDZH8/748738219890/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })

        # Sends a POST request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/team/delete', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data.decode(), "Error has occurred, The specified team does not exist")

    def test_delete_existent_team(self):
        """
        This tries to delete a existing team.
        The expected outcome is the return statement '200 OK'
        And an error message
        ''
        """

        # Python dictionary
        json_obj = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "UMU0VNH09",
            "user_name": "elias.renman",
            "command": "/erdemo",
            "text": "delete team01",
            "response_url": "https://hooks.slack.com/commands/TM1TFDZH8/748738219890/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })

        # Sends a POST request to the endpoint "/delete_team/" with the payload of json_obj.
        self.app.post('/team/create', json=json_obj)
        rv = self.app.post('/team/delete', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data.decode(), "Team successfully deleted")

    def test_update_existing_team(self):
        """
        This tries to updating an existing team.
        The expected outcome is the return statement '200 OK'
        And a success message of
        'Team name successfully updated'
        """

        # This parses dictionary to a json.
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team0",
        })

        self.app.post('/team/create', json=json_obj)
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team0 Team01",
        })

        # Sends a POST request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/team/update', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data.decode(), "Team name successfully updated")

    def test_update_non_existing_team(self):
        """
        This tries to updating an non existing team.
        The expected outcome is the return statement '200 OK'
        And a error message of:
        'Error has occurred, The specified team does not exist or something went wrong'
        """
        # This parses dictionary to a json.
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team_does_not_exist Team_still_does_not_exist",
        })

        # Sends a POST request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/team/update', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data.decode(),
                         "Error has occurred, The specified team does not exist or something went wrong")

    def test_display_team(self):
        """
        This tries to create a team.
        Then prints a list of all teams.
        The expected outcome is the return statement '200 OK'
        And the message 'Here's a list of all teams.\n  *test_Team'
        """

        # Python dictionary
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "test_Team"
        })

        # Sends a POST request to the endpoint "/delete_team/" with the payload of json_obj.
        self.app.post('/team/create', json=json_obj)
        rv = self.app.post('/team/display', json=json_obj)

        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        print(rv.data.decode())
        self.assertTrue(len(rv.data.decode()) > 0)

    def test_team_id(self):
        """
        Tries to run get_team_id function to get it to run.
        """
        from Routes.team_routes import get_team_id
        get_team_id("new Team0")
