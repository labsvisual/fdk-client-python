"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .CartItemMeta import CartItemMeta











from .OpenApiFiles import OpenApiFiles

from .MultiTenderPaymentMethod import MultiTenderPaymentMethod












class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    employee_discount = fields.Float(required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    cod_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    discount = fields.Float(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    quantity = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    extra_meta = fields.Dict(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    product_id = fields.Int(required=False)
    

