"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CouponValidity(BaseSchema):
    # Cart swagger.json

    
    valid = fields.Boolean(required=False)
    
    display_message_en = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

