"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DefaultKeyRequest(BaseSchema):
    # Catalog swagger.json

    
    default_key = fields.Str(required=False)
    

