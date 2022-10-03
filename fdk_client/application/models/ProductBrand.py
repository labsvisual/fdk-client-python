"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Media import Media

from .ProductListingAction import ProductListingAction


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

