"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductAction import ProductAction

from .CategoryInfo import CategoryInfo





from .BaseInfo import BaseInfo



from .ProductImage import ProductImage




class CartProduct(BaseSchema):
    # Cart swagger.json

    
    action = fields.Nested(ProductAction, required=False)
    
    categories = fields.List(fields.Nested(CategoryInfo, required=False), required=False)
    
    name = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    brand = fields.Nested(BaseInfo, required=False)
    
    type = fields.Str(required=False)
    
    images = fields.List(fields.Nested(ProductImage, required=False), required=False)
    
    slug = fields.Str(required=False)
    

