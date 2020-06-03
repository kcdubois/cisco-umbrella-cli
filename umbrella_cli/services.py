"""
    Umbrella API service class and custom exceptions.
"""

import logging

import requests

from umbrella_cli import serializers
from umbrella_cli import models


class ManagementApiService:
    _base_url = "https://management.api.umbrella.com/v1"
    _headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    _endpoint = "organizations/{}/"
    _schema = serializers.BaseSerializer
    _model = None
    _id = None
    
    def _authenticate(self, access, secret):
        """ Returns the Basic Authorization object"""
        return requests.auth.HTTPBasicAuth(access, secret)

    def __init__(self, access, secret, org_id):
        self.org_id = org_id
        self.auth = self._authenticate(access, secret)

    def _get_absolute_url(self, *args):
        """ Returns the full URL based on the endpoint property """
        return "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id),
            *args
        ))

    def get(self, obj_id):
        """ Generic GET method for single object """
        url = self._get_absolute_url(obj_id)

        response = requests.get(
            url=url, auth=self.auth, headers=self._headers,
            verify=False
        )
        if response.status_code == 200:
            return self._schema().load(response.json())
        
        response.raise_for_status()

    def get_list(self, filter={}):
        """ Generic GET method for single object """
        url = self._get_absolute_url()

        response = requests.get(
            url=url, auth=self.auth, headers=self._headers,
            verify=False
        )

        if response.status_code == 200:
            return self._schema(many=True).load(response.json())

        response.raise_for_status()

    def create(self, obj):
        """ Generic POST method for creating a new object """
        url = self._get_absolute_url()

        payload = self._schema().dump(obj)

        response = requests.post(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if response.status_code == 200:
            return self._schema().load(response.json())
         
        response.raise_for_status()

    def update(self, obj):
        """ Generic POST method for updating an object """
        url = self._get_absolute_url(getattr(obj, self._id))
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
        url = self._get_absolute_url(getattr(obj, self._id))

        payload = self._schema().dump(obj)

        response = requests.delete(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if response.status_code == 204:
            return self._schema().load(response.json())

        response.raise_for_status()


class SitesEndpointService(ManagementApiService):
    _endpoint = "organizations/{}/sites"
    _schema = serializers.SiteSerializer
    _model = models.Site
    _id = "site_id"


class InternalNetworkService(ManagementApiService):
    """
    API Service representing the Internal Network endpoint 
    """
    _endpoint = "organizations/{}/internalnetworks"
    _schema = serializers.InternalNetworkSerializer
    _model = models.InternalNetwork
    _id = "internal_network_id"
