# TO DO: Add comments before each function to describe what is happening. 

#!/usr/bin/env python3
# Adding in unittests RankDomain microservice.
import os
import unittest
import rankServer
import json

from unittest import mock

class RankDomainTestCase(unittest.TestCase):

    # Get the url from the server application.
    def get(self, url):
        self.app = rankServer.app.test_client()
        return self.app.get(url)

    # Test whether the get command requests the 402 endpoint.
    def test_success(self):
        response = self.get('/domain_rank')
        self.assertEqual(response.status_code, 402)

    # Test whether the get command requests the 402 endpoint and gets a 200 status update.
    @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
                 return_value=True)
    def test_pay_success(self, *args):
        response = self.get('/domain_rank?url=google.com')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
