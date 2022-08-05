"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class AddBeneficiaryViaOtpVerificationRequest(BaseSchema):
    # Payment swagger.json

    
    hash_key = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

