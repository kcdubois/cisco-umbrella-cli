# Umbrella CLI

Umbrella CLI is a CLI tool to help with interacting with the Cisco Umbrella API for batch jobs and information retrieval.

## Getting Started

To start using Umbrella CLI, you must first create an API key and API secret in your Umbrella dashboard, as well as retrieving your organization ID. You can copy the project, spin up a new Pipenv virtual environment and get started with Umbrella CLI.

```
git clone https://gitlab.com/kcdubois/umbrella-cli
pipenv install
pipenv shell
cd umbrella-cli
umbrella-cli.py version
```

### Installing

The package is now available on Pypi, it is now possible to install it using pip.

```
pip install cisco-umbrella-cli
umbrella-cli --help
```


### Built with

* [requests](https://2.python-requests.org/en/master/) - Library to manage the API calls
* [marshmallow](https://marshmallow.readthedocs.io/en/stable/) - Object serialization
* [click](https://click.palletsprojects.com/en/7.x/) - CLI commands parsing