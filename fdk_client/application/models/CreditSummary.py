"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .BalanceDetails import BalanceDetails






class CreditSummary(BaseSchema):
    # Payment swagger.json

    
    status = fields.Str(required=False)
    
    balance = fields.Nested(BalanceDetails, required=False)
    
    merchant_customer_ref_id = fields.Str(required=False)
    
    status_message = fields.Str(required=False)
    

