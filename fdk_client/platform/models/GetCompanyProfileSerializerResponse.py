"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BusinessDetails import BusinessDetails



from .BusinessCountryInfo import BusinessCountryInfo

from .GetAddressSerializer import GetAddressSerializer





from .Document import Document

from .UserSerializer import UserSerializer

from .UserSerializer import UserSerializer



from .UserSerializer import UserSerializer



from .ContactDetails import ContactDetails










class GetCompanyProfileSerializerResponse(BaseSchema):
    # CompanyProfile swagger.json

    
    business_type = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    mode = fields.Str(required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    business_details = fields.Nested(BusinessDetails, required=False)
    
    business_info = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Nested(Document, required=False), required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    company_type = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    name = fields.Str(required=False)
    
    contact_details = fields.Nested(ContactDetails, required=False)
    
    created_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    warnings = fields.Dict(required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    

