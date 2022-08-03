"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .LadderPrice import LadderPrice




class LadderOfferItem(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    min_quantity = fields.Int(required=False)
    
    max_quantity = fields.Int(required=False)
    
    price = fields.Nested(LadderPrice, required=False)
    
    margin = fields.Int(required=False)
    

