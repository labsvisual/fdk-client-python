"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CancelPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    status_code = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    success = fields.Boolean(required=False)
    

