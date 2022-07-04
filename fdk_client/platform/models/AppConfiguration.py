"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ConfigurationProduct import ConfigurationProduct

from .ConfigurationListing import ConfigurationListing






class AppConfiguration(BaseSchema):
    # Catalog swagger.json

    
    app_id = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    config_type = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    

