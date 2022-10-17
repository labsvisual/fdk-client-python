"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class InventoryPage(BaseSchema):
    # Catalog swagger.json

    
    next_id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    has_next = fields.Boolean(required=False)
    
    has_previous = fields.Boolean(required=False)
    
    item_total = fields.Int(required=False)
    

