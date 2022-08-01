"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .UserSerializer import UserSerializer









from .UserSerializer import UserSerializer









from .UserSerializer import UserSerializer





from .BrandBannerSerializer import BrandBannerSerializer




class GetBrandResponseSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    mode = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    reject_reason = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    warnings = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    verified_by = fields.Nested(UserSerializer, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    verified_on = fields.Str(required=False)
    

