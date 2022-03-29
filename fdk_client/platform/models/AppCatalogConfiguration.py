"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ConfigurationListing import ConfigurationListing



from .ConfigurationProduct import ConfigurationProduct


class AppCatalogConfiguration(BaseSchema):
    # Catalog swagger.json

    
    config_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    listing = fields.Nested(ConfigurationListing, required=False)
    
    config_type = fields.Str(required=False)
    
    product = fields.Nested(ConfigurationProduct, required=False)
    

