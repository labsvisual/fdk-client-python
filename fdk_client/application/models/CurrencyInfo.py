"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CurrencyInfo(BaseSchema):
    # Cart swagger.json

    
    code = fields.Str(required=False)
    
    symbol = fields.Str(required=False)
    

