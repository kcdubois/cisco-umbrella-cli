"""
    This module contains the sub-commands of umbrella sites.
"""

import click
import requests
from requests.auth import HTTPBasicAuth

from umbrella_cli.serializers import SiteSerializer


BASE_URL = "https://management.api.umbrella.com/v1/"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}


@click.group()
@click.pass_context
def sites(ctx):
    pass


@sites.command()
@click.pass_context
def get(ctx):
    """ Get the list of sites """
    url = BASE_URL + "/organizations/{org_id}/sites".format(org_id=ctx.obj['ORG'])
    schema = SiteSerializer(many=True)

    response = requests.get(url, headers=HEADERS, auth=HTTPBasicAuth(ctx.obj['ACCESS'], ctx.obj['SECRET']), verify=False)

    if response.status_code == 200:
        sites = schema.load(response.json())

        for site in sites:
            click.echo("{}: {}".format(site.site_id, site.name))
    else:
        click.echo("An error occured with the Umbrella API, code {}".format(str(response.status_code)))

    