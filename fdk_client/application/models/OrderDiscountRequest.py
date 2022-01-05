"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OrderDiscountRequest(BaseSchema):
    # Rewards swagger.json

    
    currency = fields.Str(required=False)
    
    order_amount = fields.Float(required=False)
    

