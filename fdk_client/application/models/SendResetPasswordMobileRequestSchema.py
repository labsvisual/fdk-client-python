"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SendResetPasswordMobileRequestSchema(BaseSchema):
    # User swagger.json

    
    country_code = fields.Str(required=False)
    
    mobile = fields.Str(required=False)
    
    captcha_code = fields.Str(required=False)
    

