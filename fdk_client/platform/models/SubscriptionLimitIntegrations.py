"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SubscriptionLimitIntegrations(BaseSchema):
    # Billing swagger.json

    
    enabled = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    

