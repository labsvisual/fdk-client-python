"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSize import ProductSize














class ConfigurationProductConfig(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Nested(ProductSize, required=False)
    
    title = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    subtitle = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    

