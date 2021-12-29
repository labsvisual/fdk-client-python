"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderPicklistListing import OrderPicklistListing

from .PlatformOrderPage import PlatformOrderPage

from .Filters import Filters



from .AppliedFilters import AppliedFilters


class OrderDetails(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderPicklistListing, required=False), required=False)
    
    page = fields.Nested(PlatformOrderPage, required=False)
    
    filters = fields.Nested(Filters, required=False)
    
    next_order_status = fields.Dict(required=False)
    
    applied_filters = fields.Nested(AppliedFilters, required=False)
    

