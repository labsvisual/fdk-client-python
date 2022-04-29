"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PageCoupon(BaseSchema):
    # Cart swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total_item_count = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    current = fields.Int(required=False)
    

