"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CompanyByBrandsRequest(BaseSchema):
    # Configuration swagger.json

    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    

