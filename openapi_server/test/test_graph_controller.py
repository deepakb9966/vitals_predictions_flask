# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.future_values_get200_response import FutureValuesGet200Response  # noqa: E501
from openapi_server.models.message_dto import MessageDto  # noqa: E501
from openapi_server.test import BaseTestCase


class TestGraphController(BaseTestCase):
    """GraphController integration test stubs"""

    def test_future_values_get(self):
        """Test case for future_values_get

        
        """
        query_string = [('step_length', 56)]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/future_values',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
