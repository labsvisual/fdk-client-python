"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BrandCompanyInfo(BaseSchema):
    # Configuration swagger.json

    
    company_name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

