"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InvoiceDetailsStatusTrail(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    

