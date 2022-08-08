"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentMethodsMeta import PaymentMethodsMeta


class CreateOrderUserPaymentMethods(BaseSchema):
    # Payment swagger.json

    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(PaymentMethodsMeta, required=False)
    

