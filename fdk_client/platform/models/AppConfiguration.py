"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ConfigurationListing import ConfigurationListing

from .ConfigurationProduct import ConfigurationProduct








class AppConfiguration(BaseSchema):
    # Catalog swagger.json

    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    app_id = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    

