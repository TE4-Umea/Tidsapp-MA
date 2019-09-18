import unittest
import json
import flask
from timer import app


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_delete_non_existent_project(self):
        """
        This tries to delete a non existent project.
        Expected outcome is a return status of 200 and a error message saying.
        `Error has occurred, The specified project does not exist`
        """
        # Python dictionary
        payload = {
            "token": "UzM1Hasfas231sdcUZrVbD76JpmP",
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POSt request to the endpoint "/delete_project/" with the payload of json_obj.
        rv = self.app.post('/delete_project/', json=json_obj)

        # Makes sure that the response status is 200.
        assert rv.status == '200 OK'
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified project does not exist")
