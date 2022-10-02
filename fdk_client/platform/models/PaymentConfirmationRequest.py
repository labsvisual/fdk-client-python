"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .MultiTenderPaymentMethod import MultiTenderPaymentMethod




class PaymentConfirmationRequest(BaseSchema):
    # Payment swagger.json

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    order_id = fields.Str(required=False)
    

