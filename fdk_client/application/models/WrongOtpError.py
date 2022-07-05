"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class WrongOtpError(BaseSchema):
    # Payment swagger.json

    
    description = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Str(required=False)
    

