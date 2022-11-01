"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Page import Page



from .AbandonedCart import AbandonedCart




class AbandonedCartResponse(BaseSchema):
    # Cart swagger.json

    
    result = fields.Dict(required=False)
    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(AbandonedCart, required=False), required=False)
    
    success = fields.Boolean(required=False)
    

