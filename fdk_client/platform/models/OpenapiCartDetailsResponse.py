"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CartBreakup import CartBreakup





from .CartProductInfo import CartProductInfo


class OpenapiCartDetailsResponse(BaseSchema):
    # Cart swagger.json

    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
    is_valid = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(CartProductInfo, required=False), required=False)
    

