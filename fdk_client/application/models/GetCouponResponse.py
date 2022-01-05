"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PageCoupon import PageCoupon

from .Coupon import Coupon


class GetCouponResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(PageCoupon, required=False)
    
    available_coupon_list = fields.List(fields.Nested(Coupon, required=False), required=False)
    

