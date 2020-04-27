import unittest

from umbrella_cli import serializers

class TestUmbrellaSiteSerializer(unittest.TestCase):
    def setUp(self):
        self.json = [
            {
                "originId": 395218748,
                "isDefault": False,
                "name": "BLUE",
                "modifiedAt": "2020-04-05T19:07:38.000Z",
                "createdAt": "2020-04-05T19:07:38.000Z",
                "type": "site",
                "internalNetworkCount": 2,
                "vaCount": 4,
                "siteId": 1479824
            },
            {
                "originId": 136056751,
                "isDefault": True,
                "name": "Default Site",
                "modifiedAt": "2018-03-06T01:23:13.000Z",
                "createdAt": "2018-03-06T01:23:13.000Z",
                "type": "site",
                "internalNetworkCount": 0,
                "vaCount": 0,
                "siteId": 635875
            }]

    