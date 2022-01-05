"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AuthenticationConfig(BaseSchema):
    # Configuration swagger.json

    
    required = fields.Boolean(required=False)
    
    provider = fields.Str(required=False)
    

