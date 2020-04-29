"""
    This is the test suite for serializers and models of the Umbrella API.
"""


import unittest
import datetime as dt

from umbrella_cli import serializers, models

class TestSiteSerializer(unittest.TestCase):
    def setUp(self):
        self.single_object = """{
            "originId": 385265878,
            "isDefault": false,
            "name": "Home Office",
            "modifiedAt": "2020-03-20T18:08:36.000Z",
            "createdAt": "2020-03-20T18:08:36.000Z",
            "type": "site",
            "internalNetworkCount": 2,
            "vaCount": 2,
            "siteId": 1334164
            }"""

        self.multiple_objects = """[{
                "originId": 395218748,
                "isDefault": false,
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
                "isDefault": true,
                "name": "Default Site",
                "modifiedAt": "2018-03-06T01:23:13.000Z",
                "createdAt": "2018-03-06T01:23:13.000Z",
                "type": "site",
                "internalNetworkCount": 0,
                "vaCount": 0,
                "siteId": 635875
            }]"""

    def test_site_serialize_with_valid_single_object(self):
        """ Test a working serialization of a single object. """
        schema = serializers.SiteSerializer()
        result = schema.loads(self.single_object)

        self.assertIsInstance(result, models.Site)
        self.assertIsInstance(result.name, str)
        self.assertEqual(result.name, "Home Office")

        #! Python datetime not supporting Zulu timezone
        #self.assertIsInstance(result['created_at'], dt.datetime)
        #self.assertEqual(result['created_at'], dt.datetime(
        #    year=2020, month=4, day=5,
        #    hour=19, minute=7, second=38
        #    ))
        

        self.assertIsInstance(result.va_count, int)
        self.assertEqual(result.va_count, 2)

        self.assertIsInstance(result.is_default, bool)
        self.assertEqual(result.is_default, False)


    def test_site_serialize_with_valid_multiple_objects(self):
        """ Test a working serialization of multiple objects. """
        schema = serializers.SiteSerializer(many=True)
        result = schema.loads(self.multiple_objects)

        self.assertEqual(len(result), 2)