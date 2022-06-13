"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Child import Child

from .ProductListingAction import ProductListingAction

from .ImageUrls import ImageUrls








class CategoryItems(BaseSchema):
    # Catalog swagger.json

    
    childs = fields.List(fields.Nested(Child, required=False), required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    
    banners = fields.Nested(ImageUrls, required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

