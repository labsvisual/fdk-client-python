"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryResponse import InventoryResponse

from .Page import Page


class InventoryResponsePaginated(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(InventoryResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

