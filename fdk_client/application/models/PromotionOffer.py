"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PromotionOffer(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    
    promotion_group = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    valid_till = fields.Str(required=False)
    

