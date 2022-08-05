"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SelectCartAddressRequest(BaseSchema):
    # Cart swagger.json

    
    id = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    cart_id = fields.Str(required=False)
    

