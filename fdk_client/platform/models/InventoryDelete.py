"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryDeleteData import InventoryDeleteData




class InventoryDelete(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(InventoryDeleteData, required=False)
    
    success = fields.Boolean(required=False)
    

