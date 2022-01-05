"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SubscriptionLimitTeam(BaseSchema):
    # Billing swagger.json

    
    limit = fields.Int(required=False)
    

