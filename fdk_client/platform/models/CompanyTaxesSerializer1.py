"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CompanyTaxesSerializer1(BaseSchema):
    # CompanyProfile swagger.json

    
    rate = fields.Float(required=False)
    
    enable = fields.Boolean(required=False)
    
    effective_date = fields.Str(required=False)
    

