"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .InventoryPayload import InventoryPayload


class InventoryRequestSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    company_id = fields.Int(required=False)
    
    payload = fields.List(fields.Nested(InventoryPayload, required=False), required=False)
    

