"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .InvSize import InvSize

from .ItemQuery import ItemQuery


class InventoryRequest(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    item = fields.Nested(ItemQuery, required=False)
    

