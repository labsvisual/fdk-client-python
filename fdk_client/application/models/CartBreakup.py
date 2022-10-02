"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DisplayBreakup import DisplayBreakup

from .CouponBreakup import CouponBreakup

from .LoyaltyPoints import LoyaltyPoints

from .RawBreakup import RawBreakup


class CartBreakup(BaseSchema):
    # Cart swagger.json

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    

