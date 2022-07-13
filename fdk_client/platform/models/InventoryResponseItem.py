"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryPayload import InventoryPayload

from .InventoryFailedReason import InventoryFailedReason


class InventoryResponseItem(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(InventoryPayload, required=False)
    
    reason = fields.Nested(InventoryFailedReason, required=False)
    

