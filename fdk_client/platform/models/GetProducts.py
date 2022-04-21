"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Price import Price

from .LimitedProductData import LimitedProductData







from .Size import Size


class GetProducts(BaseSchema):
    # Catalog swagger.json

    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    price = fields.Nested(Price, required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    product_uid = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    

