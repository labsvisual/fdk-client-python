"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSerializer2 import UserSerializer2





from .UserSerializer2 import UserSerializer2

from .GetAddressSerializer import GetAddressSerializer



from .UserSerializer2 import UserSerializer2














class GetCompanySerializer(BaseSchema):
    # Catalog swagger.json

    
    verified_by = fields.Nested(UserSerializer2, required=False)
    
    stage = fields.Str(required=False)
    
    company_type = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer2, required=False)
    
    addresses = fields.List(fields.Nested(GetAddressSerializer, required=False), required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer2, required=False)
    
    business_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    verified_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    reject_reason = fields.Str(required=False)
    

