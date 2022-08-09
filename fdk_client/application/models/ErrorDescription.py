"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class ErrorDescription(BaseSchema):
    # Payment swagger.json

    
    payment_transaction_id = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    msg = fields.Str(required=False)
    
    invalid_id = fields.Boolean(required=False)
    
    merchant_name = fields.Str(required=False)
    
    cancelled = fields.Boolean(required=False)
    
    expired = fields.Boolean(required=False)
    

