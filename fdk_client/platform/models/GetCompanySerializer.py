"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .UserSerializer1 import UserSerializer1



from .UserSerializer1 import UserSerializer1

from .GetAddressSerializer import GetAddressSerializer











from .UserSerializer1 import UserSerializer1






class GetCompanySerializer(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer1, required=False)
    
    business_type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer1, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    stage = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    verified_by = fields.Nested(UserSerializer1, required=False)
    
    verified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    

