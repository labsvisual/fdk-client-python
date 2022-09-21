"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ContactDetails import ContactDetails

from .CompanyTaxesSerializer1 import CompanyTaxesSerializer1

from .BusinessDetails import BusinessDetails

from .Document import Document



from .CreateUpdateAddressSerializer import CreateUpdateAddressSerializer














class UpdateCompany(BaseSchema):
    # CompanyProfile swagger.json

    
    company_type = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer1, required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    business_info = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(CreateUpdateAddressSerializer, required=False), required=False)
    
    reject_reason = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    

