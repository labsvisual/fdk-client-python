"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CreateOrderUserData import CreateOrderUserData












class CreateOrderUserResponse(BaseSchema):
    # Payment swagger.json

    
    callback_url = fields.Str(required=False)
    
    data = fields.Nested(CreateOrderUserData, required=False)
    
    success = fields.Boolean(required=False)
    
    status_code = fields.Int(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    order_id = fields.Str(required=False)
    

