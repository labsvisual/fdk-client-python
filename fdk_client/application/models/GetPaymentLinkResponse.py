"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




















class GetPaymentLinkResponse(BaseSchema):
    # Payment swagger.json

    
    merchant_name = fields.Str(required=False)
    
    polling_timeout = fields.Int(required=False)
    
    amount = fields.Float(required=False)
    
    status_code = fields.Int(required=False)
    
    success = fields.Boolean(required=False)
    
    external_order_id = fields.Str(required=False)
    
    payment_link_current_status = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    payment_link_url = fields.Str(required=False)
    

