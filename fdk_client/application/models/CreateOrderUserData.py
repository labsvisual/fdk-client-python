"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class CreateOrderUserData(BaseSchema):
    # Payment swagger.json

    
    currency = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    email = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    

