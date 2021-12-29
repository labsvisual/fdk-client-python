"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
















class ProfileEditSuccessSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    verify_email_otp = fields.Boolean(required=False)
    
    verify_email_link = fields.Boolean(required=False)
    
    verify_mobile_otp = fields.Boolean(required=False)
    
    user = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    
    user_exists = fields.Boolean(required=False)
    

