"""
    Umbrella API service class and custom exceptions.
"""

import logging
import csv

import requests

from umbrella_cli import serializers
from umbrella_cli import models


class BaseManager:
    """
    Base manager used as a collection of a specific models.
    """
    _model = None


class RestManager(BaseManager):
    """
    Base REST manager class to generate basic CRUD operations on models.
    Apart from testing, this shouldn't be used directly.
    """
    _base_url = "https://management.api.umbrella.com/v1"
    _headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    _schema = serializers.BaseSerializer
    _model_name = None
    _id = None
    
    def _authenticate(self, access, secret):
        """ Returns the Basic Authorization object"""
        return requests.auth.HTTPBasicAuth(access, secret)

    @property
    def endpoint(self):
        """ Returns the endpoint's URL path of the manager """
        return f"organizations/{self.org_id}/{self._model_name}"

    def __init__(self, access, secret, org_id):
        self.org_id = org_id
        self.auth = self._authenticate(access, secret)

    @property
    def url(self):
        """ Returns the full URL based on the endpoint property """
        return "/".join((
            self._base_url, 
            self.endpoint
        ))

    def get(self, obj_id):
        """ Generic GET method for single object """
        url = "/".join((self.url, obj_id))

        response = requests.get(
            url=url, auth=self.auth, headers=self._headers,
            verify=False
        )

        if response.status_code == 200:
            return self._schema().load(response.json())
        
        response.raise_for_status()

    def get_list(self, filter={}):
        """ Generic GET method for single object """
        response = requests.get(
            url=self.url, auth=self.auth, headers=self._headers,
            verify=False
        )

        if response.status_code == 200:
            return self._schema(many=True).load(response.json())

        response.raise_for_status()

    def create(self, obj):
        """ Generic POST method for creating a new object """
        payload = self._schema().dump(obj)
        
        response = requests.post(
            url=self.url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if response.status_code == 200:
            return self._schema().load(response.json())
         
        response.raise_for_status()

    def update(self, obj):
        """ Generic POST method for updating an object """
        url = "/".join(
            (self.url, getattr(obj, self._id))
        )
        payload = self._schema().dump(obj)

        response = requests.put(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )
        
        if response.status_code == 200:
            return self._schema().load(response.json())

        response.raise_for_status()

    def delete(self, obj):
        """ Generic DELETE method for deleting an object """
        url = "/".join(
            (self.url, getattr(obj, self._id))
        )

        payload = self._schema().dump(obj)

        response = requests.delete(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if response.status_code == 204:
            return self._schema().load(response.json())

        response.raise_for_status()


class SitesManager(RestManager):
    """
    API Service representing the Sites endpoint.
    """
    _model_name = "sites"
    _schema = serializers.SiteSerializer
    _model = models.Site
    _id = "site_id"


class InternalNetworkManager(RestManager):
    """
    API Service representing the Internal Network endpoint.
    """
    _model_name = "internalnetworks"
    _schema = serializers.InternalNetworkSerializer
    _model = models.InternalNetwork
    _id = "internal_network_id"



class CsvManager(BaseManager):
    """
    Base CSV Manager to help with import and export of models from the API.
    """

    def __init__(self, fp, delimiter=","):
        self._csv_lines = []

        try:
            with open(fp) as csvfile:
                reader = csv.DictReader(csvfile)
                for line in reader:
                    self._csv_lines.append(line)
        except IOError:
            raise




    
