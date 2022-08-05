"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Child import Child





from .ImageUrls import ImageUrls

from .ProductListingAction import ProductListingAction


class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

