"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ResendOrCancelPaymentRequest(BaseSchema):
    # Payment swagger.json

    
    request_type = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

