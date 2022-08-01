"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ProductSize import ProductSize








class ConfigurationProductVariantConfig(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    size = fields.Nested(ProductSize, required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    display_type = fields.Str(required=False)
    

