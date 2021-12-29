"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .InvoiceDetailsPaymentMethodsData import InvoiceDetailsPaymentMethodsData




class InvoiceDetailsPaymentMethods(BaseSchema):
    # Billing swagger.json

    
    id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    pg_payment_method_id = fields.Str(required=False)
    
    data = fields.Nested(InvoiceDetailsPaymentMethodsData, required=False)
    
    is_default = fields.Boolean(required=False)
    

