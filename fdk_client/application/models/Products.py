"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .Size import Size

from .ProductDetails import ProductDetails



from .Price1 import Price1


class Products(BaseSchema):
    # Catalog swagger.json

    
    max_quantity = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    
    product_uid = fields.Int(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    price = fields.Nested(Price1, required=False)
    

