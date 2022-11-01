"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    order_items = fields.List(fields.Dict(required=False), required=False)
    
    aggregator = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    payload = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    phone_number = fields.Str(required=False)
    
    merchant_params = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    

