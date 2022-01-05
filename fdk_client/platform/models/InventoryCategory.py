"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryCategory(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    categories = fields.List(fields.Raw(required=False), required=False)
    

