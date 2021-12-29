"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Subscription import Subscription


class SubscriptionActivateRes(BaseSchema):
    # Billing swagger.json

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(Subscription, required=False)
    

