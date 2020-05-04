"""
    Umbrella API service class.
"""

import requests

from umbrella_cli import serializers

class ApiError(Exception):
    pass

class ManagementApiService:
    BASE_URL = "https://management.api.umbrella.com/v1"
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    def __init__(self, org_id):
        self.org_id = org_id

    def get_sites(self):
        """ Returns a single site or all sites """
        url = self.BASE_URL + "/organizations/{org_id}/sites".format(
            org_id=self.org_id
        )

        schema = serializers.SiteSerializer(many=True)

        response = requests.get(url, headers=self.HEADERS, verify=False)

        if response.status_code == 200:
            return schema.load(response.json())
        else:
            raise ApiError("An error occured with the API: {code}".format(
                code=response.status_code
            ))