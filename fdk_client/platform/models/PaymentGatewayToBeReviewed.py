"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PaymentGatewayToBeReviewed(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.List(fields.Str(required=False), required=False)
    
    success = fields.Boolean(required=False)
    

