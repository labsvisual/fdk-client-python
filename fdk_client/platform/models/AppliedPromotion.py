"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class AppliedPromotion(BaseSchema):
    # Cart swagger.json

    
    promotion_type = fields.Str(required=False)
    
    mrp_promotion = fields.Boolean(required=False)
    
    offer_text = fields.Str(required=False)
    
    amount = fields.Float(required=False)
    
    article_quantity = fields.Int(required=False)
    
    promo_id = fields.Str(required=False)
    

