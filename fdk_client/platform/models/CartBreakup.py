"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RawBreakup import RawBreakup

from .DisplayBreakup import DisplayBreakup

from .CouponBreakup import CouponBreakup

from .LoyaltyPoints import LoyaltyPoints


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    raw = fields.Nested(RawBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    

