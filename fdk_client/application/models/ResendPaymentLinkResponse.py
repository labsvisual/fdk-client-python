"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ResendPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    polling_timeout = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    

