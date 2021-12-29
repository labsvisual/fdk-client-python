"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TaxLinesPriceSetPresentmentMoney(BaseSchema):
    # Order swagger.json

    
    currency_code = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    

