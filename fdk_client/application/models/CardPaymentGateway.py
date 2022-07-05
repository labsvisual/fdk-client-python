"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CardPaymentGateway(BaseSchema):
    # Payment swagger.json

    
    aggregator = fields.Str(required=False)
    
    api = fields.Str(required=False)
    
    customer_id = fields.Str(required=False)
    

