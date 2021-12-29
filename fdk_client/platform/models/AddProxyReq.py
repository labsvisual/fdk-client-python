"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AddProxyReq(BaseSchema):
    # Partner swagger.json

    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    

