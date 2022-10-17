"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PaymentMethodsMeta(BaseSchema):
    # Payment swagger.json

    
    payment_identifier = fields.Str(required=False)
    
    payment_gateway = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    

