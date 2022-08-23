"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ConfigurationListingSortConfig(BaseSchema):
    # Catalog swagger.json

    
    is_active = fields.Boolean(required=False)
    
    priority = fields.Int(required=False)
    
    key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

