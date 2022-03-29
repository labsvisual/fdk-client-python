"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductImage import ProductImage









from .ProductAction import ProductAction

from .BaseInfo import BaseInfo

from .CategoryInfo import CategoryInfo


class CartProduct(BaseSchema):
    # Cart swagger.json

    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    

