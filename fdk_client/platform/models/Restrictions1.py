"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PostOrder1 import PostOrder1



from .UserRegistered import UserRegistered









from .PromotionPaymentModes import PromotionPaymentModes

from .UsesRestriction1 import UsesRestriction1


class Restrictions1(BaseSchema):
    # Cart swagger.json

    
    post_order = fields.Nested(PostOrder1, required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    user_registered = fields.Nested(UserRegistered, required=False)
    
    anonymous_users = fields.Boolean(required=False)
    
    order_quantity = fields.Int(required=False)
    
    user_groups = fields.List(fields.Int(required=False), required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    payments = fields.List(fields.Nested(PromotionPaymentModes, required=False), required=False)
    
    uses = fields.Nested(UsesRestriction1, required=False)
    

