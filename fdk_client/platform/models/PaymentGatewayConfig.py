"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PaymentGatewayConfig(BaseSchema):
    # Payment swagger.json

    
    merchant_salt = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    secret = fields.Str(required=False)
    

