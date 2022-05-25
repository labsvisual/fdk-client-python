"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CompanyTax(BaseSchema):
    # CompanyProfile swagger.json

    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    

