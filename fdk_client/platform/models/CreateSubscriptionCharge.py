"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ChargeLineItem import ChargeLineItem






class CreateSubscriptionCharge(BaseSchema):
    # Billing swagger.json

    
    name = fields.Str(required=False)
    
    trial_days = fields.Int(required=False)
    
    line_items = fields.List(fields.Nested(ChargeLineItem, required=False), required=False)
    
    is_test = fields.Boolean(required=False)
    
    return_url = fields.Str(required=False)
    

