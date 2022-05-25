"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class OfferPrice(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    marked = fields.Int(required=False)
    
    bulk_effective = fields.Float(required=False)
    
    effective = fields.Int(required=False)
    
    currency_symbol = fields.Str(required=False)
    

