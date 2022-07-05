"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ConfigurationListingSortConfig(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    

