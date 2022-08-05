"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ShippingAddress import ShippingAddress

from .CartItem import CartItem


class OpenApiCartServiceabilityRequest(BaseSchema):
    # Cart swagger.json

    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    cart_items = fields.Nested(CartItem, required=False)
    

