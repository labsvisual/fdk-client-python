"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .LoyaltyPoints import LoyaltyPoints

from .DisplayBreakup import DisplayBreakup

from .RawBreakup import RawBreakup

from .CouponBreakup import CouponBreakup


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    

