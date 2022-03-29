"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CheckValidityResponse(BaseSchema):
    # Billing swagger.json

    
    is_valid = fields.Boolean(required=False)
    
    discount_amount = fields.Float(required=False)
    

