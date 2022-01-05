"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ReqBodyVerifyOTPShipment(BaseSchema):
    # Order swagger.json

    
    request_id = fields.Str(required=False)
    
    otp_code = fields.Str(required=False)
    

