"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Subscription import Subscription


class SubscriptionStatus(BaseSchema):
    # Billing swagger.json

    
    is_enabled = fields.Boolean(required=False)
    
    subscription = fields.Nested(Subscription, required=False)
    

