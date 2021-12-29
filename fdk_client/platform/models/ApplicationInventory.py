"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppInventoryConfig import AppInventoryConfig

from .AuthenticationConfig import AuthenticationConfig

from .ArticleAssignmentConfig import ArticleAssignmentConfig

from .RewardPointsConfig import RewardPointsConfig

from .AppCartConfig import AppCartConfig

from .AppPaymentConfig import AppPaymentConfig

from .AppOrderConfig import AppOrderConfig

from .AppLogisticsConfig import AppLogisticsConfig









from .LoyaltyPointsConfig import LoyaltyPointsConfig










class ApplicationInventory(BaseSchema):
    # Configuration swagger.json

    
    inventory = fields.Nested(AppInventoryConfig, required=False)
    
    authentication = fields.Nested(AuthenticationConfig, required=False)
    
    article_assignment = fields.Nested(ArticleAssignmentConfig, required=False)
    
    reward_points = fields.Nested(RewardPointsConfig, required=False)
    
    cart = fields.Nested(AppCartConfig, required=False)
    
    payment = fields.Nested(AppPaymentConfig, required=False)
    
    order = fields.Nested(AppOrderConfig, required=False)
    
    logistics = fields.Nested(AppLogisticsConfig, required=False)
    
    business = fields.Str(required=False)
    
    comms_enabled = fields.Boolean(required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    _id = fields.Str(required=False)
    
    loyalty_points = fields.Nested(LoyaltyPointsConfig, required=False)
    
    app = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    

