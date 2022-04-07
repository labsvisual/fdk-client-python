"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .GetCatalogConfigurationDetailsProduct import GetCatalogConfigurationDetailsProduct







from .GetCatalogConfigurationDetailsSchemaListing import GetCatalogConfigurationDetailsSchemaListing


class EntityConfiguration(BaseSchema):
    # Catalog swagger.json

    
    config_id = fields.Str(required=False)
    
    product = fields.Nested(GetCatalogConfigurationDetailsProduct, required=False)
    
    config_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    listing = fields.Nested(GetCatalogConfigurationDetailsSchemaListing, required=False)
    

