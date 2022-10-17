"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class WalletOtpResponse(BaseSchema):
    # Payment swagger.json

    
    request_id = fields.Str(required=False)
    
    is_verified_flag = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

