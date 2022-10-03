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

    
    name = fields.Str(required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    slug = fields.Str(required=False)
    

