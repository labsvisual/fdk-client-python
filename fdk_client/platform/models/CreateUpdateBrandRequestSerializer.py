"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .BrandBannerSerializer import BrandBannerSerializer












class CreateUpdateBrandRequestSerializer(BaseSchema):
    # CompanyProfile swagger.json

    
    _locale_language = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    
    banner = fields.Nested(BrandBannerSerializer, required=False)
    
    logo = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    description = fields.Str(required=False)
    
    brand_tier = fields.Str(required=False)
    

