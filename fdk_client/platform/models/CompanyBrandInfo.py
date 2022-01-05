"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CompanyBrandInfo(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    brand_logo_url = fields.Str(required=False)
    
    brand_banner_url = fields.Str(required=False)
    
    brand_banner_portrait_url = fields.Str(required=False)
    

