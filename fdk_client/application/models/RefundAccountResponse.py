"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class RefundAccountResponse(BaseSchema):
    # Payment swagger.json

    
    data = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    is_verified_flag = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    

