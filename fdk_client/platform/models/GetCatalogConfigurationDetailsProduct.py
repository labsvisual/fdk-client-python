"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class GetCatalogConfigurationDetailsProduct(BaseSchema):
    # Catalog swagger.json

    
    detail = fields.Dict(required=False)
    
    compare = fields.Dict(required=False)
    
    variant = fields.Dict(required=False)
    
    similar = fields.Dict(required=False)
    

