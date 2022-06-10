"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


























class PaymentInitializationRequest(BaseSchema):
    # Payment swagger.json

    
    vpa = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    method = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    timeout = fields.Int(required=False)
    
    aggregator = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    

