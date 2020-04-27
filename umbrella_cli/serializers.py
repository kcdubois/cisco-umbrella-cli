"""
    This module contains all the Schema objects for the Umbrella Management
    API to interact with the response object as Python native constructs. 
"""

from marshmallow import Schema, fields


class UmbrellaSite(Schema):
    """ Umbrella internal site serializer """
    origin_id = fields.Integer(dump_only=True, data_key="originId")
    name = fields.String()
    site_id = fields.Integer(dump_only=True, data_key="siteId")
    default = fields.Boolean(dump_only=True)
    type = fields.String(dump_only=True)
    internal_network_count = fields.Integer(dump_only=True, data_key="internalNetworkCount")
    va_count = fields.Integer(dump_only=True, data_key="vaCount")
    modified_at = fields.DateTime(format="rfc", dump_only=True, data_key="modifiedAt")
    created_at = fields.DateTime(format="rfc", dump_only=True, data_key="createdAt")

