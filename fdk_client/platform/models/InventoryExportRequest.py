"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class InventoryExportRequest(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    

