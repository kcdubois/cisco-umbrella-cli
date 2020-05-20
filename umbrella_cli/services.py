"""
    Umbrella API service class and custom exceptions.
"""

import logging

import requests

from umbrella_cli import serializers
from umbrella_cli import models


class ApiError(Exception): pass
class ApiAuthenticationError(ApiError): pass
class ApiNotFoundError(ApiError): pass


class ManagementApiService:
    _base_url = "https://management.api.umbrella.com/v1"
    _headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    _endpoint = "/organizations/{}/"
    _schema = serializers.BaseSerializer
    _model = None
    _id = None
    
    def _authenticate(self, access, secret):
        """ Returns the Basic Authorization object"""
        return requests.auth.HTTPBasicAuth(access, secret)

    def __init__(self, access, secret, org_id):
        self.org_id = org_id
        self.auth = self._authenticate(access, secret)

    def _check_response_code(self, response):
        """ Raises an exception based on the status_code property """
        if response.status_code == 200:
            return True
        elif response.status_code == 401:
            raise ApiAuthenticationError(
                "An authentication error occured. Please check your API keys."
            )
        elif response.status_code == 404:
            raise ApiNotFoundError("The URL is not found. Is your URL valid?")
        else:
            raise ApiError("An error occured with the API: {code}:{body}".format(
                code=response.status_code,
                body=response.text
            ))

    def get(self, obj_id):
        """ Generic GET method for single object """
        url = "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id), 
            obj_id
        ))

        response = requests.get(
            url=url, auth=self.auth, headers=self._headers,
            verify=False
        )
        if self._check_response_code(response):
            return self._schema().load(response.json())

    def get_list(self, filter={}):
        """ Generic GET method for single object """
        url = "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id)
        ))

        response = requests.get(
            url=url, auth=self.auth, headers=self._headers,
            verify=False
        )

        if self._check_response_code(response):
            return self._schema(many=True).load(response.json())


    def create(self, obj):
        """ Generic POST method for creating a new object """
        url = "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id)
        ))

        payload = self._schema().dump(obj)

        response = requests.post(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if self._check_response_code(response):
            return self._schema().load(response.json())
         
    def update(self, obj):
        """ Generic POST method for updating an object """
        url = "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id), 
            getattr(obj, self._id)
        ))
        payload = self._schema().dump(obj)

        response = requests.put(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )
        
        if self._check_response_code(response):
            return self._schema().load(response.json())

    def delete(self, obj):
        """ Generic DELETE method for deleting an object """
        url = "/".join((
            self._base_url, 
            self._endpoint.format(self.org_id), 
            getattr(obj, self._id)
        ))

        payload = self._schema().dump(obj)

        response = requests.delete(
            url=url, auth=self.auth, headers=self._headers,
            json=payload, verify=False
        )

        if self._check_response_code(response):
            return self._schema().load(response.json())


class SitesEndpointService(ManagementApiService):
    _endpoint = "organizations/{}/sites"
    _schema = serializers.SiteSerializer
    _model = models.Site
    _id = "site_id"
