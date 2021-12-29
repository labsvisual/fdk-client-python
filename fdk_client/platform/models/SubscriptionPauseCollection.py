"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SubscriptionPauseCollection(BaseSchema):
    # Billing swagger.json

    
    behavior = fields.Str(required=False)
    
    resume_at = fields.Str(required=False)
    

