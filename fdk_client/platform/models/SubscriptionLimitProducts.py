"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SubscriptionLimitProducts(BaseSchema):
    # Billing swagger.json

    
    bulk = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    

