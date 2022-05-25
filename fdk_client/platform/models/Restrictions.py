"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PostOrder import PostOrder







from .UsesRestriction import UsesRestriction

from .BulkBundleRestriction import BulkBundleRestriction

from .PriceRange import PriceRange


class Restrictions(BaseSchema):
    # Cart swagger.json

    
    ordering_stores = fields.List(fields.Int(required=False), required=False)
    
    payments = fields.Dict(required=False)
    
    post_order = fields.Nested(PostOrder, required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    coupon_allowed = fields.Boolean(required=False)
    
    uses = fields.Nested(UsesRestriction, required=False)
    
    bulk_bundle = fields.Nested(BulkBundleRestriction, required=False)
    
    price_range = fields.Nested(PriceRange, required=False)
    

