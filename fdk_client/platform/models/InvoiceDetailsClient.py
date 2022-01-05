"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class InvoiceDetailsClient(BaseSchema):
    # Billing swagger.json

    
    address_lines = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    

