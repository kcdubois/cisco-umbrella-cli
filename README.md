# Umbrella CLI
[![Build Status](https://travis-ci.org/kcdubois/cisco-umbrella-cli.svg?branch=master)](https://travis-ci.org/kcdubois/cisco-umbrella-cli)

Umbrella CLI is a CLI tool to help with interacting with the Cisco Umbrella API for batch jobs and information retrieval.

## Getting Started

To start using Umbrella CLI, you must first create an API key and API secret in your Umbrella dashboard, as well as retrieving your organization ID. You can copy the project, spin up a new Pipenv virtual environment and get started with Umbrella CLI.

```
pip install cisco-umbrella-cli
umbrella-cli --help
```


### Built with

* [requests](https://2.python-requests.org/en/master/) - Library to manage the API calls
* [marshmallow](https://marshmallow.readthedocs.io/en/stable/) - Object serialization
* [click](https://click.palletsprojects.com/en/7.x/) - CLI commands parsing
