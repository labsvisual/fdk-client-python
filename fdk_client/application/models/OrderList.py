"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderSchema import OrderSchema

from .OrderPage import OrderPage

from .OrderFilters import OrderFilters


class OrderList(BaseSchema):
    # Order swagger.json

    
    items = fields.List(fields.Nested(OrderSchema, required=False), required=False)
    
    page = fields.Nested(OrderPage, required=False)
    
    filters = fields.Nested(OrderFilters, required=False)
    

