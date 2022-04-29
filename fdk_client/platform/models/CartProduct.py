"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductAction import ProductAction

from .BaseInfo import BaseInfo

from .CategoryInfo import CategoryInfo





from .ProductImage import ProductImage




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    name = fields.Str(required=False)
    
    action = fields.Nested(ProductAction, required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    type = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    uid = fields.Int(required=False)
    

