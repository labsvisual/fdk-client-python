"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class InvoicesDataClient(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    address_lines = fields.List(fields.Str(required=False), required=False)
    

