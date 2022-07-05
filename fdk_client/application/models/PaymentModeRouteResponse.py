"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PaymentOptionAndFlow import PaymentOptionAndFlow




class PaymentModeRouteResponse(BaseSchema):
    # Payment swagger.json

    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    
    success = fields.Boolean(required=False)
    

