"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class BeneficiaryModeDetails(BaseSchema):
    # Payment swagger.json

    
    branch_name = fields.Str(required=False)
    
    vpa = fields.Str(required=False)
    
    wallet = fields.Str(required=False)
    
    comment = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    account_no = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    bank_name = fields.Str(required=False)
    
    account_holder = fields.Str(required=False)
    
    ifsc_code = fields.Str(required=False)
    
    address = fields.Str(required=False)
    

