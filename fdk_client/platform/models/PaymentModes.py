"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .PaymentAllowValue import PaymentAllowValue




class PaymentModes(BaseSchema):
    # Cart swagger.json

    
    networks = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    
    uses = fields.Nested(PaymentAllowValue, required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    

