"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SetDefaultBeneficiaryRequest(BaseSchema):
    # Payment swagger.json

    
    order_id = fields.Str(required=False)
    
    beneficiary_id = fields.Str(required=False)
    

