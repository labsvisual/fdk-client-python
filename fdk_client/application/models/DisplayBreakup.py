"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class DisplayBreakup(BaseSchema):
    # Cart swagger.json

    
    currency_symbol = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    
    message = fields.List(fields.Str(required=False), required=False)
    

