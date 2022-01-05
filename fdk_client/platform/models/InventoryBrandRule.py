"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryBrandRule(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Int(required=False), required=False)
    

