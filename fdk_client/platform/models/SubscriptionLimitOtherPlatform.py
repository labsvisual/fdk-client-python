"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SubscriptionLimitOtherPlatform(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    

