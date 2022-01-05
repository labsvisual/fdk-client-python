"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .RewardPointsConfig import RewardPointsConfig

from .AppCartConfig import AppCartConfig

from .AppPaymentConfig import AppPaymentConfig

from .LoyaltyPointsConfig import LoyaltyPointsConfig




class AppInventoryPartialUpdate(BaseSchema):
    # Configuration swagger.json

    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    
    cart = fields.Nested(AppCartConfig, required=False)
    
    payment = fields.Nested(AppPaymentConfig, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPointsConfig, required=False)
    
    comms_enabled = fields.Boolean(required=False)
    

