import os

import requests
import click
from requests.auth import HTTPBasicAuth
from marshmallow import Schema

requests.urllib3.disable_warnings()


BASE_URL = "https://management.api.umbrella.com/v1"
HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}



@click.group()
@click.option("--access", prompt="Enter your API Access key", help="Umbrella API Access Key")
@click.option("--secret", prompt="Enter your API Secret key", hide_input=True, help="Umbrella API Secret Key")
@click.option("--org", prompt="Enter your organization ID", help="Umbrella Organizaton ID")
@click.pass_context
def cli(ctx, access, secret, org):
    ctx.ensure_object(dict)

    ctx.obj['ACCESS'] = access
    ctx.obj['SECRET'] = secret
    ctx.obj['ORG'] = org


@click.command()
@click.pass_context
def get_sites(ctx):
    """ Get the list of sites using the basic auth string and orgID """
    url = BASE_URL + "/organizations/{orgID}/sites".format(orgID=ctx.obj['ORG'])

    response = requests.get(url, headers=HEADERS, auth=HTTPBasicAuth(ctx.obj['ACCESS'], ctx.obj['SECRET']), verify=False)

    if response.status_code == 200:
        sites = response.json()

        for site in sites:
            click.echo("{}: {}".format(site['siteId'], site['name']))
    else:
        click.echo("An error occured with the Umbrella API, code {}".format(str(response.status_code)))


@click.command()
@click.argument("sitelist", help="")
@click.pass_context
def import_sites(ctx, sitelist):
    """ Import a list of sites into Umbrella """
    pass




# Adding commands to group
cli.add_command(get_sites)


if __name__ == "__main__":
    cli(obj={})