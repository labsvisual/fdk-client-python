"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    message = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    uid = fields.Str(required=False)
    

