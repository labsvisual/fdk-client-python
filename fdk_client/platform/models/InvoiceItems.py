"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .InvoiceItemsPlan import InvoiceItemsPlan







from .InvoiceItemsPeriod import InvoiceItemsPeriod














class InvoiceItems(BaseSchema):
    # Billing swagger.json

    
    _id = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    plan = fields.Nested(InvoiceItemsPlan, required=False)
    
    name = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    period = fields.Nested(InvoiceItemsPeriod, required=False)
    
    unit_amount = fields.Float(required=False)
    
    amount = fields.Float(required=False)
    
    type = fields.Str(required=False)
    
    invoice_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    

