"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StoreByBrandsRequest(BaseSchema):
    # Configuration swagger.json

    
    company_id = fields.Int(required=False)
    
    brands = fields.Int(required=False)
    
    search_text = fields.Str(required=False)
    

