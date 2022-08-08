"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductDetails import ProductDetails







from .Size import Size





from .Price1 import Price1




class Products(BaseSchema):
    # Catalog swagger.json

    
    product_details = fields.Nested(ProductDetails, required=False)
    
    product_uid = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    min_quantity = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    price = fields.Nested(Price1, required=False)
    
    auto_select = fields.Boolean(required=False)
    

