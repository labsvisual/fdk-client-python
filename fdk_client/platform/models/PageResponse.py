"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class PageResponse(BaseSchema):
    # Catalog swagger.json

    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    
    current = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    size = fields.Int(required=False)
    

