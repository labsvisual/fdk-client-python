"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CategoryInfo import CategoryInfo



from .ProductAction import ProductAction

from .ProductImage import ProductImage



from .BaseInfo import BaseInfo




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    uid = fields.Int(required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    slug = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    name = fields.Str(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
