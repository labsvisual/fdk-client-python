"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class PaymentStatusUpdateRequest(BaseSchema):
    # Payment swagger.json

    
    method = fields.Str(required=False)
    
    amount = fields.Int(required=False)
    
    email = fields.Str(required=False)
    
    merchant_order_id = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    contact = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    

