"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BrandBannerSerializer import BrandBannerSerializer












class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    brand_tier = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    _locale_language = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    

