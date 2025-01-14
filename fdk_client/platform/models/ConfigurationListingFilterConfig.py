"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ConfigurationListingFilterValue import ConfigurationListingFilterValue












class ConfigurationListingFilterConfig(BaseSchema):
    # Catalog swagger.json

    
    type = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value_config = fields.Nested(ConfigurationListingFilterValue, required=False)
    
    display_name = fields.Str(required=False)
    
    priority = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    logo = fields.Str(required=False)
    

