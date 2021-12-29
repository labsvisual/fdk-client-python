"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .EntitySubscription import EntitySubscription




class CreateSubscriptionResponse(BaseSchema):
    # Billing swagger.json

    
    subscription = fields.Nested(EntitySubscription, required=False)
    
    confirm_url = fields.Str(required=False)
    

