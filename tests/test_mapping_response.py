__author__ = 'omarsubhiabdelhafith'

import os
import unittest

from mockpy.models.mapping_response import BodyResponse


class MappingResponseTests(unittest.TestCase):

    def test_mapping_response_loads_from_file(self):
        body = BodyResponse({"body_file": "contactus.json"}, os.path.dirname(__file__) + "/res")
        assert "officeDetails" in body.read_value()

        assert body.body_type == BodyResponse.FILE

    def test_mapping_response_loads_from_yml(self):
        body = BodyResponse({"body": "test test test"}, os.path.dirname(__file__) + "/res")
        value = body.read_value()
        assert "test test test" in value

        body = BodyResponse({"body": {"key": "value"}}, os.path.dirname(__file__) + "/res")
        value = body.read_value()
        assert "key" in value

        body = BodyResponse({"body": ["v1", "v2"]}, os.path.dirname(__file__) + "/res")
        value = body.read_value()
        assert "v1" in value

        assert body.body_type == BodyResponse.RAW

    def test_mapping_returns_an_image(self):
        body = BodyResponse({"body_image": "cat.png"}, os.path.dirname(__file__) + "/res")
        assert body.body_type == BodyResponse.IMAGE

    def test_has_correct_file_name_for_file(self):
        body = BodyResponse({"body_file": "test2.json"}, os.path.dirname(__file__) + "/res")
        assert body.file_name == "test2.json"

    def test_has_correct_file_name_for_object(self):
        body = BodyResponse({"body": "test test test"}, os.path.dirname(__file__) + "/res")
        assert body.file_name == ""

    def test_has_correct_file_name_for_image(self):
        body = BodyResponse({"body_image": "cat.png"}, os.path.dirname(__file__) + "/res")
        assert body.file_name == "cat.png"
