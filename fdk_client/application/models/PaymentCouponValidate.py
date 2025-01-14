"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponValidity import CouponValidity






class PaymentCouponValidate(BaseSchema):
    # Cart swagger.json

    
    coupon_validity = fields.Nested(CouponValidity, required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    

