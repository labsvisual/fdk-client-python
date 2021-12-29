"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ReferralDetailsUser(BaseSchema):
    # Rewards swagger.json

    
    blocked = fields.Boolean(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referral_code = fields.Str(required=False)
    

