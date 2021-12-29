"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityChargePrice(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    

