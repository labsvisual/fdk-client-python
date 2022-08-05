"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SubscriptionPaymentMethodResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.List(fields.Dict(required=False), required=False)
    
    success = fields.Boolean(required=False)
    

