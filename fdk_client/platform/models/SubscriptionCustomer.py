"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Phone import Phone

from .SubscriptionBillingAddress import SubscriptionBillingAddress


















class SubscriptionCustomer(BaseSchema):
    # Billing swagger.json

    
    phone = fields.Nested(Phone, required=False)
    
    billing_address = fields.Nested(SubscriptionBillingAddress, required=False)
    
    _id = fields.Str(required=False)
    
    unique_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    

