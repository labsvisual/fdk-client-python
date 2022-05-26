"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ContactDetails import ContactDetails







from .UserSerializer import UserSerializer













from .Document import Document

from .UserSerializer import UserSerializer



from .BusinessCountryInfo import BusinessCountryInfo

from .UserSerializer import UserSerializer

from .BusinessDetails import BusinessDetails





from .GetAddressSerializer import GetAddressSerializer




class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    taxes = fields.List(fields.Dict(required=False), required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    verified_on = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    created_on = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    modified_on = fields.Str(required=False)
    
    business_info = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    stage = fields.Str(required=False)
    

