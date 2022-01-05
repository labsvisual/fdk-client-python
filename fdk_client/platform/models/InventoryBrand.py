"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryBrand(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    

