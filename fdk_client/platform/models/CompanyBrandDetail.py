"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class CompanyBrandDetail(BaseSchema):
    # Catalog swagger.json

    
    brand_id = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    brand_name = fields.Str(required=False)
    
    total_article = fields.Int(required=False)
    

