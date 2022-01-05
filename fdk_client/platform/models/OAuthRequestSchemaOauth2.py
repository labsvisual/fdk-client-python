"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OAuthRequestSchemaOauth2(BaseSchema):
    # User swagger.json

    
    access_token = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
    refresh_token = fields.Str(required=False)
    

