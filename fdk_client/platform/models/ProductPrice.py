"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class ProductPrice(BaseSchema):
    # Cart swagger.json

    
    marked = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    add_on = fields.Float(required=False)
    
    selling = fields.Float(required=False)
    
    effective = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    

