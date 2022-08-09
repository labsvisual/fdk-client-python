"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ChargeCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    verified = fields.Boolean(required=False)
    
    amount = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

