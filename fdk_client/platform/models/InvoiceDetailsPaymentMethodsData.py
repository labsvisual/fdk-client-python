"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .InvoiceDetailsPaymentMethodsDataChecks import InvoiceDetailsPaymentMethodsDataChecks









from .InvoiceDetailsPaymentMethodsDataNetworks import InvoiceDetailsPaymentMethodsDataNetworks







from .InvoiceDetailsPaymentMethodsDataThreeDSecureUsage import InvoiceDetailsPaymentMethodsDataThreeDSecureUsage


class InvoiceDetailsPaymentMethodsData(BaseSchema):
    # Billing swagger.json

    
    brand = fields.Str(required=False)
    
    last4 = fields.Str(required=False)
    
    checks = fields.Nested(InvoiceDetailsPaymentMethodsDataChecks, required=False)
    
    wallet = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    funding = fields.Str(required=False)
    
    exp_year = fields.Int(required=False)
    
    networks = fields.Nested(InvoiceDetailsPaymentMethodsDataNetworks, required=False)
    
    exp_month = fields.Int(required=False)
    
    fingerprint = fields.Str(required=False)
    
    generated_from = fields.Str(required=False)
    
    three_d_secure_usage = fields.Nested(InvoiceDetailsPaymentMethodsDataThreeDSecureUsage, required=False)
    

