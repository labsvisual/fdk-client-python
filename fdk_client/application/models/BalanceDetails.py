"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class BalanceDetails(BaseSchema):
    # Payment swagger.json

    
    formatted_value = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    value = fields.Float(required=False)
    

