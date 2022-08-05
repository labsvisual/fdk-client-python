"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class Coupon(BaseSchema):
    # Cart swagger.json

    
    expires_on = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    is_applicable = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    coupon_code = fields.Str(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    title = fields.Str(required=False)
    
    coupon_value = fields.Float(required=False)
    

