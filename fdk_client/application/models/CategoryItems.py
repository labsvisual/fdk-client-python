"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls

from .Child import Child



from .ProductListingAction import ProductListingAction






class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    

