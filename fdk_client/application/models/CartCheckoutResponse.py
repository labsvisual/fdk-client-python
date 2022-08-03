"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CheckCart import CheckCart














class CartCheckoutResponse(BaseSchema):
    # Cart swagger.json

    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CheckCart, required=False)
    
    data = fields.Dict(required=False)
    
    order_id = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    callback_url = fields.Str(required=False)
    
    app_intercept_url = fields.Str(required=False)
    
    payment_confirm_url = fields.Str(required=False)
    

