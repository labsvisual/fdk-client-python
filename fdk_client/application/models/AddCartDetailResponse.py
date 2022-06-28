"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CartDetailResponse import CartDetailResponse




class AddCartDetailResponse(BaseSchema):
    # Cart swagger.json

    
    partial = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    cart = fields.Nested(CartDetailResponse, required=False)
    
    message = fields.Str(required=False)
    

