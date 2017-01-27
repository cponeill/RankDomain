#!/usr/bin/env python3
# Adding in unittests RankDomain microservice.
import os
import unittest
import rankServer
import json

from unittest import mock

class RankDomainTestCase(unittest.TestCase):

    def get(self, url):
        self.app = rankServer.app.test_client()
        return self.app.get(url)

    def test_success(self):
        response = self.get('/domain_rank')
        self.assertEqual(response.status_code, 402)

    # Will add in 200 endpoint tomorrow
    # @mock.patch('two1.bitserv.flask.decorator.Payment.contains_payment',
              # return_value=True)

if __name__ == '__main__':
    unittest.main()
