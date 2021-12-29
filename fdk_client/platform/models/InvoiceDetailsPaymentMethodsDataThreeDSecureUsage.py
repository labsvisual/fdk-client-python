"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class InvoiceDetailsPaymentMethodsDataThreeDSecureUsage(BaseSchema):
    # Billing swagger.json

    
    supported = fields.Boolean(required=False)
    

