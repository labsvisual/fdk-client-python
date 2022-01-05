"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InvoiceDetailsPaymentMethodsDataChecks(BaseSchema):
    # Billing swagger.json

    
    cvc_check = fields.Str(required=False)
    
    address_line1_check = fields.Str(required=False)
    
    address_postal_code_check = fields.Str(required=False)
    

