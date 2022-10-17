"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class DeleteApplicationUserRequestSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    reason_id = fields.Str(required=False)
    
    request_id = fields.Str(required=False)
    
    otp = fields.Str(required=False)
    

