"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class VerifyOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    request_id = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

