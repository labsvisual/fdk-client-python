"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class AddProxyResponse(BaseSchema):
    # Partner swagger.json

    
    _id = fields.Str(required=False)
    
    attached_path = fields.Str(required=False)
    
    proxy_url = fields.Str(required=False)
    
    company_id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    extension_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    

