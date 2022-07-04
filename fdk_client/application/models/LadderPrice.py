"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class LadderPrice(BaseSchema):
    # Cart swagger.json

    
    effective = fields.Int(required=False)
    
    currency_code = fields.Str(required=False)
    
    offer_price = fields.Float(required=False)
    
    currency_symbol = fields.Str(required=False)
    
    marked = fields.Int(required=False)
    

