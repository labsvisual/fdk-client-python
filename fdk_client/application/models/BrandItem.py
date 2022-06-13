"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductListingAction import ProductListingAction

from .ImageUrls import ImageUrls



from .Media import Media










class BrandItem(BaseSchema):
    # Catalog swagger.json

    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    uid = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    

