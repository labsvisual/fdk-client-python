"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class RedeemReferralCodeResponse(BaseSchema):
    # Rewards swagger.json

    
    message = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referrer_id = fields.Str(required=False)
    
    referrer_info = fields.Str(required=False)
    

