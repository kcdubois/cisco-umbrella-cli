"""
This modules includes all the tests related to Click cubcommands.
"""

from unittest import mock
import pytest
from click.testing import CliRunner

from umbrella_cli import cli


class TestSitesCommands:

    @pytest.fixture
    def credentials(self):
        return [
            "--access ACCESS_KEY",
            "--secret SECRET_KEY",
            "--org 1234567"
        ]

    @mock.patch("umbrella_cli.services")
    def test_sites_list(self, mock_api_service, credentials):
        runner = CliRunner()
        
        
        result = runner.invoke(cli, credentials + ["sites", "list"])
