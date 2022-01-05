"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InvoiceItemsPlanRecurring(BaseSchema):
    # Billing swagger.json

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Int(required=False)
    

