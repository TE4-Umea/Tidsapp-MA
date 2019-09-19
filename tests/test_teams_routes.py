import unittest
import json
import flask
from timer import app


class TestCreateTeam(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_team(self):
        '''
        This tries to create a team.
        The expected outcome is the return statement '200 OK'
        And the message 'Created team successfully'
        '''

        # Python dictionary
        payload = {
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team0"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POSt request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/create_team/', json=json_obj)

        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Created team successfully")

    def test_delete_non_existent_team(self):
        '''
        This tries to delete a non existent team.
        The expected outcome is the return statement '200 OK'
        And an error message
        'Error has occurred, The specified team does not exist'
        '''

        # Python dictionary
        payload = {
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
        }

        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POSt request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/delete_team/', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified team does not exist")

    def test_update_existing_team(self):
        '''
        This tries to updating an existing team.
        The expected outcome is the return statement '200 OK'
        And if no teams exist the statement
        'The specified team does not exist'
        '''

        # This parses dictionary to a json.
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team0",
        })

        self.app.post('/create_team/', json=json_obj)
        json_obj = json.dumps({
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "Team0 Team01",
        })

        # Sends a POSt request to the endpoint "/delete_team/" with the payload of json_obj.
        rv = self.app.post('/update_team/', json=json_obj)
        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "The specified team does not exist")

    def test_display_team(self):
        '''
        This tries to create a team.
        Then prints a list of all teams.
        The expected outcome is the return statement '200 OK'
        And the message 'Heres a list of all teams.\n  *test_Team'
        '''

        # Python dictionary
        payload = {
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
            "text": "test_Team"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POSt request to the endpoint "/delete_team/" with the payload of json_obj.
        self.app.post('/create_team/', json=json_obj)
        rv = self.app.post('/display_team/', json=json_obj)

        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Heres a list of all teams.\n * test_Team")











    # def test_delete_non_existent_project(self):
    #     """
    #     This tries to delete a non existent project.
    #     Expected outcome is a return status of 200 and a error message saying.
    #     `Error has occurred, The specified project does not exist`
    #     """
    #     # Python dictionary
    #     payload = {
    #         "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
    #     }
    #     # This parses dictionary to a json.
    #     json_obj = json.dumps(payload)
    #
    #     # Sends a POSt request to the endpoint "/delete_project/" with the payload of json_obj.
    #     rv = self.app.post('/delete_project/', json=json_obj)
    #
    #     # Makes sure that the response status is 200.
    #     assert rv.status == '200 OK'
    #     # Asserts that the response is the what is expected.
    #     self.assertEqual(rv.data, "Error has occurred, The specified project does not exist")
