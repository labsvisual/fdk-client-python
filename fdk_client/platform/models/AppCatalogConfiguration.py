"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ConfigurationListing import ConfigurationListing

from .ConfigurationProduct import ConfigurationProduct


















class AppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    
    modified_by = fields.Dict(required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    config_id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    

