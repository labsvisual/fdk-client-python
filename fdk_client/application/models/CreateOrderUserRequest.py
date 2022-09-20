"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .CreateOrderUserPaymentMethods import CreateOrderUserPaymentMethods






class CreateOrderUserRequest(BaseSchema):
    # Payment swagger.json

    
    failure_callback_url = fields.Str(required=False)
    
    success_callback_url = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    payment_methods = fields.Nested(CreateOrderUserPaymentMethods, required=False)
    
    meta = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    

