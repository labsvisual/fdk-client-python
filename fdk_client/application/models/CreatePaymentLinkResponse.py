"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CreatePaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    polling_timeout = fields.Int(required=False)
    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    payment_link_id = fields.Str(required=False)
    
    payment_link_url = fields.Str(required=False)
    

