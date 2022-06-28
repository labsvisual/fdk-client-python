"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .OfferPrice import OfferPrice










class OfferItem(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    total = fields.Float(required=False)
    
    price = fields.Nested(OfferPrice, required=False)
    
    best = fields.Boolean(required=False)
    
    auto_applied = fields.Boolean(required=False)
    
    margin = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    

