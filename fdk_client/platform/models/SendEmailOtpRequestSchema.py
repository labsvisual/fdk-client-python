"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class SendEmailOtpRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    register_token = fields.Str(required=False)
    

