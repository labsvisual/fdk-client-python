"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class OptinCompanyDetail(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    company_type = fields.Str(required=False)
    
    business_type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

