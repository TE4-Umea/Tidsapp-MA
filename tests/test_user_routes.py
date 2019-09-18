import unittest
import json
import flask

import util
from timer import app


class TestCreateProject(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.token = util.get_env("token")

