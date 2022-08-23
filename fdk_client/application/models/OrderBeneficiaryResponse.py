"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OrderBeneficiaryDetails import OrderBeneficiaryDetails




class OrderBeneficiaryResponse(BaseSchema):
    # Payment swagger.json

    
    beneficiaries = fields.List(fields.Nested(OrderBeneficiaryDetails, required=False), required=False)
    
    show_beneficiary_details = fields.Boolean(required=False)
    

