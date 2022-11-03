"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductListingAction import ProductListingAction



from .Media import Media


class ProductBrand(BaseSchema):
    # Catalog swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    

