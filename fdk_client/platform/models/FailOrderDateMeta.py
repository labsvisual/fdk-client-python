"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class FailOrderDateMeta(BaseSchema):
    # Order swagger.json

    
    added_on_store = fields.Str(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

