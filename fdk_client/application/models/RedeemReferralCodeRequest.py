"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RedeemReferralCodeRequest(BaseSchema):
    # Rewards swagger.json

    
    device_id = fields.Str(required=False)
    
    referral_code = fields.Str(required=False)
    

