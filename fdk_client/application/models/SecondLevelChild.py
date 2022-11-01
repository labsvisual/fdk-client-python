"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ImageUrls import ImageUrls

from .ThirdLevelChild import ThirdLevelChild









from .ProductListingAction import ProductListingAction


class SecondLevelChild(BaseSchema):
    # Catalog swagger.json

    
    banners = fields.Nested(ImageUrls, required=False)
    
    childs = fields.List(fields.Nested(ThirdLevelChild, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(ProductListingAction, required=False)
    

