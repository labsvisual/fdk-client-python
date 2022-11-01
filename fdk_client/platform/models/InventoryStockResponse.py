"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InventoryPage import InventoryPage


class InventoryStockResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(InventoryPage, required=False)
    

