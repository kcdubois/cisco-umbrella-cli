"""
    This module contains the sub-commands of umbrella sites.
"""

import click
import requests
from requests.auth import HTTPBasicAuth

from umbrella_cli import services
from umbrella_cli.models import Site

@click.group()
@click.pass_context
def sites(ctx):
    pass


@sites.command(name="get-all")
@click.pass_context
def get_all(ctx):
    """ Get the list of sites """
    api = services.SitesEndpointService(
        access=ctx.obj["ACCESS"], 
        secret=ctx.obj["SECRET"], 
        org_id=ctx.obj["ORG"]
    )
    
    try:
        sites = api.get_list()

        click.echo("""
+===============================================+
|+++ Umbrella Sites for Organization {org} +++|
|===============================================|
| Site ID | Name                                |
|-----------------------------------------------|""".format(org=ctx.obj['ORG'])
        )
        for site in sites:
            click.echo("| {:8}| {:36}|".format(str(site.site_id), site.name))
        
        click.echo("+===============================================+")

    except services.ApiError as error:
        click.secho(str(error), fg="yellow")
    except Exception as error:
        click.secho(str(error), fg="red")

@sites.command()
@click.argument("name")
@click.pass_context
def create(ctx, name):
    """ Create a new site """
    api = services.SitesEndpointService(
        access=ctx.obj["ACCESS"], 
        secret=ctx.obj["SECRET"], 
        org_id=ctx.obj["ORG"]
    )

    try:
        site = Site(name)

        result = api.create(site)

        click.secho("New site created with ID {id}".format(id=result.site_id),
                    fg="green")
    except services.ApiError as error:
        click.secho(str(error), fg="yellow")
    except Exception as error:
        click.secho(str(error), fg="red")
    