"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ChargeCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    transaction_token = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    verified = fields.Boolean(required=False)
    
    order_id = fields.Str(required=False)
    

