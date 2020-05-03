"""
    This module contains the test cases of the different commands supported by
    this tool.
"""

from unittest import mock

import pytest

from umbrella_cli import services

class TestManagementApiService:

    @mock.patch("umbrella_cli.services.requests")
    def test_get_sites_ok(self, mock_requests):
        api = services.ManagementApiService(1234567)

        assert api.org_id == 1234567
        
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.json.return_value = [
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

        sites = api.get_sites()

        mock_requests.get.assert_called_with(
            api.BASE_URL + "/organizations/1234567/sites",
            headers=api.HEADERS,
            verify=False
        )

    
    @mock.patch("umbrella_cli.services.requests")
    def test_get_sites_404(self, mock_requests):
        api = services.ManagementApiService(1234567)

        mock_requests.get.return_value.status_code = 404

        with pytest.raises(services.ApiError):
            api.get_sites()

        

