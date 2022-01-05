"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TotalDiscountSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    

