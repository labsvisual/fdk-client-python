"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class PaymentSelectionLock(BaseSchema):
    # Cart swagger.json

    
    enabled = fields.Boolean(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    default_options = fields.Str(required=False)
    

