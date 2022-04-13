"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


































class PaymentInitializationResponse(BaseSchema):
    # Payment swagger.json

    
    aggregator_order_id = fields.Str(required=False)
    
    bqr_image = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    virtual_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    upi_poll_url = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    status = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    timeout = fields.Int(required=False)
    
    method = fields.Str(required=False)
    
    polling_url = fields.Str(required=False)
    
    razorpay_payment_id = fields.Str(required=False)
    

