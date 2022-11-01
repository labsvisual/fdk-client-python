"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Price1(BaseSchema):
    # Catalog swagger.json

    
    currency_code = fields.Str(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

