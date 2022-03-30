"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .MultiTenderPaymentMeta import MultiTenderPaymentMeta


class MultiTenderPaymentMethod(BaseSchema):
    # Payment swagger.json

    
    mode = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    meta = fields.Nested(MultiTenderPaymentMeta, required=False)
    
