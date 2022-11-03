"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ProductDetails import ProductDetails



from .ProductGroupPrice import ProductGroupPrice





from .Size import Size




class ProductInGroup(BaseSchema):
    # Catalog swagger.json

    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    product_details = fields.Nested(ProductDetails, required=False)
    
    auto_select = fields.Boolean(required=False)
    
    price = fields.Nested(ProductGroupPrice, required=False)
    
    product_uid = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    min_quantity = fields.Int(required=False)
    

