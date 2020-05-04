"""
    This module contains the sub-commands of umbrella sites.
"""

import click
import requests
from requests.auth import HTTPBasicAuth

from umbrella_cli.services import ManagementApiService, ApiError


@click.group()
@click.pass_context
def sites(ctx):
    pass


@sites.command()
@click.pass_context
def list(ctx):
    """ Get the list of sites """
    api = ManagementApiService(ctx.obj["ORG"])
    
    try:
        sites = api.get_sites()

        click.echo(
            """
            ---------------------------------------------
            +++ Umbrella Sites for Organization {org} +++
            ---------------------------------------------
            """.format(org=ctx.obj['ORG'])
        )
        for site in sites:
            click.echo("{}: {}".format(site.site_id, site.name))
        
        click.echo("---------------------------------------------")

    except ApiError as error:
        click.secho(str(error), fg="red")

    