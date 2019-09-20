import unittest
import json
import os
from timer import app


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        from dotenv import load_dotenv
        load_dotenv()
        self.app = app.test_client()
        self.token = os.getenv("token")

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
        rv = self.app.post('/user/status', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertTrue(len(rv.data) > 0)

    def test_bad_token_user_status(self):
        """
        This tries to check a users status with a bad token.
        Expected outcome is a return status of 200 and an error message saying.
        `Error has occurred, The specified token is invalid`
        """
        # Python dictionary
        payload = {
            "token": self.token
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/status', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified token is invalid")

    def test_user_track(self):
        """
        This toggles tracking the users time.
        Expected outcome is a return status of 200 and a message saying one of two things.
        `Success. Time tracking is now active.` or `Success. Time tracking is now inactive.`
        """
        # Python dictionary
        payload = {
            "token": self.token,
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
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/track', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertTrue(
            rv.data.decode() == "Success. Time tracking is now active." or rv.data.decode() == "Success. Time tracking is now inactive.")

    def test_bad_token_user_track(self):
        """
        This tries toggling tracking the users time with a bad token.
        Expected outcome is a return status of 200 and an error message saying.
        `Error has occurred, The specified token is invalid`
        """
        # Python dictionary
        payload = {
            "token": self.token,
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
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/track', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data, "Error has occurred, The specified token is invalid")

    def test_user_join_project(self):
        """
        This allows the user to join a project of their choosing.
        Expected outcome is a return status of 200 and a message saying:
        `Project successfully joined.`
        """
        # Python dictionary
        payload = {
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFADSS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "test_project_that_exists",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        }
        # This parses dictionary to a json.
        json_obj = json.dumps(payload)

        self.app.post('/project/create', json=json_obj)
        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/join/project', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data.decode(), "Project successfully joined.")

    def test_user_join__nonexistent_project(self):
        """
        This tries to join a nonexistent project
        Expected outcome is a return status of 200 and an error message saying:
        `Error has occurred. The specified project does not exist.`
        """
        # Python dictionary cast to json.
        json_obj = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFADSS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "test_project_that_does_not_exists",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/join/project', json=json_obj)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data.decode(), "Error has occurred. The specified project does not exist.")

    def test_user_join_team(self):
        """
        This allows the user to join a team of their choosing.
        Expected outcome is a return status of 200 and a message saying:
        `Team successfully joined.`
        """
        # Python dictionary cast to json.
        payload = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFADSS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "test_team",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })
        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/join/team', json=payload)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data.decode(), 'Team successfully joined.')

    def test_user_join__nonexistent_team(self):
        """
        This tries to join a nonexistent team
        Expected outcome is a return status of 200 and an error message saying:
        `Error has occurred. The specified team does not exist.`
        """
        # Python dictionary
        payload = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFAS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })

        # Sends a POST request to the endpoint "/user_status/" with the payload of json_obj.
        rv = self.app.post('/user/join/team', json=payload)

        # Makes sure that the response status is 200.
        self.assertTrue(rv.status == '200 OK')
        # Asserts that the response is what is expected.
        self.assertEqual(rv.data.decode(), "Error has occurred. The specified team does not exist.")

    def test_user_check_non_existent(self):
        """
        This test will check whether a non existent user exists in the database.
        Expected response: 'False'
        """
        from Routes.user_routes import user_exists

        self.assertTrue(not user_exists("U2U0VFasAS09"))

    def test_user_check(self):
        """
        This test will check whether a existent user exists in the database.
        Expected response: 'False'
        """
        from Routes.user_routes import user_exists
        payload = json.dumps({
            "token": self.token,
            "team_id": "TM1TFDZH8",
            "team_domain": "te4umea",
            "channel_id": "DN0C7A2G0",
            "channel_name": "directmessage",
            "user_id": "U2U0VFAS09",
            "user_name": "test.testsson",
            "command": "\/erdemo",
            "text": "",
            "response_url": "https:\/\/hooks.slack.com\/commands\/TM1TFDZH8\/748738219890\/YGPnRsJuBqhFn5jHycboGC2C",
            "trigger_id": "755103228097.715933475586.073d00750e4e59c7f463f2c0e9587b42"
        })
        self.assertTrue(user_exists("U2U0VFAS09"))

    def test_parse_name(self):
        """
        This tests that the parse name function parses names correctly.
        Expected input in this format, 'test.testsson' expected output 'Test Testsson'.
        """
        from Routes.user_routes import parse_name
        self.assertEqual(parse_name("test.testsson"), "Test Testsson")
