"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DeliveryCharges import DeliveryCharges












class AppCartConfig(BaseSchema):
    # Configuration swagger.json

    
    delivery_charges = fields.Nested(DeliveryCharges, required=False)
    
    enabled = fields.Boolean(required=False)
    
    max_cart_items = fields.Int(required=False)
    
    min_cart_value = fields.Float(required=False)
    
    bulk_coupons = fields.Boolean(required=False)
    
    revenue_engine_coupon = fields.Boolean(required=False)
    

