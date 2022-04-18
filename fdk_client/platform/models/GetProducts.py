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

    
    product_uid = fields.Int(required=False)
    
    price = fields.Nested(Price, required=False)
    
    max_quantity = fields.Int(required=False)
    
    product_details = fields.Nested(LimitedProductData, required=False)
    
    sizes = fields.List(fields.Nested(Size, required=False), required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    min_quantity = fields.Int(required=False)
    
    allow_remove = fields.Boolean(required=False)
    
    auto_select = fields.Boolean(required=False)
    

