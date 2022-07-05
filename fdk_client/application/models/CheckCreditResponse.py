"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreditDetail import CreditDetail




class CheckCreditResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Nested(CreditDetail, required=False)
    
    success = fields.Boolean(required=False)
    

