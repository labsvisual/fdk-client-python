"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .OpenApiFiles import OpenApiFiles













from .MultiTenderPaymentMethod import MultiTenderPaymentMethod





from .CartItemMeta import CartItemMeta












class OpenApiOrderItem(BaseSchema):
    # Cart swagger.json

    
    loyalty_discount = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    discount = fields.Float(required=False)
    
    product_id = fields.Int(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    price_effective = fields.Float(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    coupon_effective_discount = fields.Float(required=False)
    
    employee_discount = fields.Float(required=False)
    
    meta = fields.Nested(CartItemMeta, required=False)
    
    cod_charges = fields.Float(required=False)
    
    size = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price_marked = fields.Float(required=False)
    
    amount_paid = fields.Float(required=False)
    

