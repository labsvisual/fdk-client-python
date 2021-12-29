"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InvoiceDetailsPeriod import InvoiceDetailsPeriod

from .InvoiceDetailsClient import InvoiceDetailsClient



























from .InvoiceDetailsStatusTrail import InvoiceDetailsStatusTrail















from .InvoicePaymentMethod import InvoicePaymentMethod


class InvoiceDetails(BaseSchema):
    # Billing swagger.json

    
    period = fields.Nested(InvoiceDetailsPeriod, required=False)
    
    client = fields.Nested(InvoiceDetailsClient, required=False)
    
    auto_advance = fields.Boolean(required=False)
    
    currency = fields.Str(required=False)
    
    paid = fields.Boolean(required=False)
    
    attemp = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    collection_method = fields.Str(required=False)
    
    subscriber_id = fields.Str(required=False)
    
    invoice_url = fields.Str(required=False)
    
    number = fields.Str(required=False)
    
    pg_data = fields.Dict(required=False)
    
    receipt_number = fields.Str(required=False)
    
    statement_descriptor = fields.Str(required=False)
    
    current_status = fields.Str(required=False)
    
    status_trail = fields.List(fields.Nested(InvoiceDetailsStatusTrail, required=False), required=False)
    
    subtotal = fields.Float(required=False)
    
    total = fields.Float(required=False)
    
    subscription = fields.Str(required=False)
    
    next_action_time = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    hash_identifier = fields.Str(required=False)
    
    payment_method = fields.Nested(InvoicePaymentMethod, required=False)
    

