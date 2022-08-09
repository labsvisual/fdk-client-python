"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class OptinCompanyMetrics(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.Int(required=False)
    
    store = fields.Int(required=False)
    
    company = fields.Str(required=False)
    

