"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StoreFilter(BaseSchema):
    # Inventory swagger.json

    
    include_tags = fields.List(fields.Str(required=False), required=False)
    
    exclude_tags = fields.List(fields.Str(required=False), required=False)
    
    query = fields.Dict(required=False)
    

