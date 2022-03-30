"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CouponBreakup import CouponBreakup

from .DisplayBreakup import DisplayBreakup

from .LoyaltyPoints import LoyaltyPoints

from .RawBreakup import RawBreakup


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
