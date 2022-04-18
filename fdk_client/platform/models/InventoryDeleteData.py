"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InventoryDeleteData(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    location_id = fields.Int(required=False)
    

