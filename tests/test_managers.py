"""
    This module contains the test cases of the different commands supported by
    this tool.
"""

from unittest import mock

import pytest
from requests.auth import HTTPBasicAuth
from requests import HTTPError

from umbrella_cli import managers
from umbrella_cli import models

class TestRestManager:

    """
        Pytest fixtures
    """

    def test_get_absolute_url(self):
        """ 
        Check that the URL constructed from the base URL and endpoint is valid
        """
        expected_url = (
            "https://management.api.umbrella.com/v1"
            "/organizations/1234567/None"
        )
        api = managers.RestManager("ACCESS", "SECRET", 1234567)

        assert expected_url == api.url

    @mock.patch("umbrella_cli.managers.requests.get")
    def test_get_sites_ok(self, mock_requests, sites):
        """ Test the GET sites with valid data """
        api = managers.SitesManager("ACCESS", "SECRET", 1234567)

        assert api.org_id == 1234567
        
        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = sites

        api.get_list()

        mock_requests.assert_called_with(
            url=(
                "https://management.api.umbrella.com"
                "/v1/organizations/1234567/sites"
            ),
            auth=HTTPBasicAuth("ACCESS", "SECRET"),
            headers=api._headers,
            verify=False
        )

    @mock.patch("umbrella_cli.managers.requests.post")
    def test_create_site_with_valid_data(self, mock_requests, site):
        """ Create a site with valid data """
        api = managers.SitesManager("ACCESS", "SECRET", 1234567)

        mock_requests.return_value.status_code = 200
        mock_requests.return_value.json.return_value = site

        site = models.Site(name="Test")

        result = api.create(site)

        mock_requests.assert_called_with(
            url=(
                "https://management.api.umbrella.com"
                "/v1/organizations/1234567/sites"
            ),
            auth=HTTPBasicAuth("ACCESS", "SECRET"),
            headers=api._headers,
            json={"name":"Test"},
            verify=False
        )

        assert result.name == "Test"
        assert result.origin_id == 395218748
        assert result.internal_network_count == 2
        

class TestSitesManager:
    def test_internal_network_service_url(self):
        """ Validate the generated URL """
        expected_url = (
            "https://management.api.umbrella.com/v1"
            "/organizations/1234567/sites"
        )

        api = managers.SitesManager("ACCESS", "SECRET", 1234567)

        assert expected_url == api.url


class TestInternalNetworksManager:
    def test_internal_network_service_url(self):
        """ Validate the generated URL """
        expected_url = (
            "https://management.api.umbrella.com/v1"
            "/organizations/1234567/internalnetworks"
        )

        api = managers.InternalNetworkManager("ACCESS", "SECRET", 1234567)

        assert expected_url == api.url
