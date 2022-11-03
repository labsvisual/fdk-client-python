"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .UserSerializer import UserSerializer



from .GetAddressSerializer import GetAddressSerializer





from .UserSerializer import UserSerializer



from .CompanyDetails import CompanyDetails











from .BusinessCountryInfo import BusinessCountryInfo



from .UserSerializer import UserSerializer


class CompanySerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    modified_on = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    business_type = fields.Str(required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    market_channels = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    notification_emails = fields.List(fields.Str(required=False), required=False)
    
    details = fields.Nested(CompanyDetails, required=False)
    
    company_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    verified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    
    business_country_info = fields.Nested(BusinessCountryInfo, required=False)
    
    created_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    

