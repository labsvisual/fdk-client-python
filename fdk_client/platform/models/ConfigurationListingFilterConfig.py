"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ConfigurationListingFilterValue import ConfigurationListingFilterValue










class ConfigurationListingFilterConfig(BaseSchema):
    # Catalog swagger.json

    
    key = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    value_config = fields.Nested(ConfigurationListingFilterValue, required=False)
    
    priority = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

