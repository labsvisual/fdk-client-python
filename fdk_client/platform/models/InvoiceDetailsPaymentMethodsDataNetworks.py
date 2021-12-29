"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InvoiceDetailsPaymentMethodsDataNetworks(BaseSchema):
    # Billing swagger.json

    
    available = fields.List(fields.Str(required=False), required=False)
    
    preferred = fields.Str(required=False)
    

