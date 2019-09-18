import unittest
import json
import flask
from timer import app
import util


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = util.get_env("token")

    def test_create_project(self):
        """
        This creates a project with the name "test_project" and checks the response.
        Expected outcome is a return status of 200 and a message saying:
        `Project successfully created. It's named: test_project`.
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "test_project"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to get the create project endpoint
        rv = self.app.post('/create_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Project successfully created. It's named: test_project")

    def test_delete_non_existent_project(self):
        """
        This tries to delete a non existent project.
        Expected outcome is a return status of 200 and a error message saying.
        `Error has occurred, The specified project does not exist`.
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "test_project0"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/delete_project/" with the payload of json_obj.
        rv = self.app.post('/delete_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified project does not exist")

    def test_delete_existent_project(self):
        """
        This tries to delete a non existent project.
        Expected outcome is a return status of 200 and a success message saying.
        `Project successfully deleted. It was named: test_project1`.
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "text": "test_project1"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POSt request to the endpoint "/delete_project/" with the payload of json_obj.
        self.app.post('/create_project/', json=json_obj)
        rv = self.app.post('/delete_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Project successfully deleted. It was named: test_project1")

    def test_update_existent_project(self):
        """
        This tries to update a existent project.
        Expected outcome is a return status of 200 and a success message saying.
        `Project successfully updated. It is now named: test_project_updated`.
        """
        rv = self.update_project("test_project2")
        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Project successfully updated. It is now named: test_project_updated")

    def test_update_non_existent_project(self):
        """
        This tries to update a non existent project.
        Expected outcome is a return status of 200 and a error message saying.
        `Error has occurred, No project exists with the name: test_project_invalid`.
        """
        rv = self.update_project("test_project_invalid")
        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Error has occurred, No project exists with the name: test_project_invalid")

    def update_project(self, find_project):
        # This parses dictionary to a json.
        json_obj = json.dumps({
            "token": self.token,
            "text": "test_project2"
        })

        # Sends a POSt request to the endpoint "/delete_project/" with the payload of json_obj.
        self.app.post('/create_project/', json=json_obj)
        json_obj = json.dumps({
            "token": self.token,
            "text": find_project + " test_project_updated"
        })
        return self.app.post('/update_project/', json=json_obj)

    def test_display_projects(self):
        """
        This tries to create a project with the name of test_project3 displays all projects as a list.
        Expected outcome is a return status of 200 and a message saying:
        `Here's a list of all the projects.\n    * test_project3`.
        """
        json_obj = json.dumps({
            "token": self.token,
            "text": "test_project3"
        })

        # Sends a POST request to get the
        self.app.post('/create_project/', json=json_obj)
        rv = self.app.post('/display_project/', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is the what is expected.
        self.assertEqual(rv.data, "Here's a list of all the projects.\n    * test_project3")
