"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ValidateCustomerRequest(BaseSchema):
    # Payment swagger.json

    
    payload = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    transaction_amount_in_paise = fields.Int(required=False)
    
    merchant_params = fields.Dict(required=False)
    
    phone_number = fields.Str(required=False)
    

