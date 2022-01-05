"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class InventoryPrice(BaseSchema):
    # Configuration swagger.json

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

