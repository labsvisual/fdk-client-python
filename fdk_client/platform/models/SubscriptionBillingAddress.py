"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class SubscriptionBillingAddress(BaseSchema):
    # Billing swagger.json

    
    country = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    line1 = fields.Str(required=False)
    
    line2 = fields.Str(required=False)
    
    postal_code = fields.Str(required=False)
    

