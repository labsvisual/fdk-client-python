"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class SendOtpResponse(BaseSchema):
    # User swagger.json

    
    resend_timer = fields.Int(required=False)
    
    resend_token = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    
    request_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    resend_email_token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    user_exists = fields.Boolean(required=False)
    

