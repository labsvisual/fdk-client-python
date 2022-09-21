"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ConfigurationListing import ConfigurationListing











from .ConfigurationProduct import ConfigurationProduct






class AppConfiguration(BaseSchema):
    # Catalog swagger.json

    
    config_type = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    config_id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

