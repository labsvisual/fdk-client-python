"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .InventoryFailedReason import InventoryFailedReason

from .InventoryPayload import InventoryPayload


class InventoryResponseItem(BaseSchema):
    # Catalog swagger.json

    
    reason = fields.Nested(InventoryFailedReason, required=False)
    
    data = fields.Nested(InventoryPayload, required=False)
    

