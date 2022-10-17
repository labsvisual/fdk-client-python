"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UserSerializer import UserSerializer

from .GetAddressSerializer import GetAddressSerializer

from .CompanyTaxesSerializer import CompanyTaxesSerializer





from .Document import Document



from .ContactDetails import ContactDetails







from .BusinessDetails import BusinessDetails



from .BusinessCountryInfo import BusinessCountryInfo

from .UserSerializer import UserSerializer





from .UserSerializer import UserSerializer






class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    uid = fields.Int(required=False)
    
    verified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    taxes = fields.List(fields.Nested(CompanyTaxesSerializer, required=False), required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    company_type = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_type = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    stage = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    

