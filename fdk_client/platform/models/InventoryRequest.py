"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ItemQuery import ItemQuery

from .InvSize import InvSize




class InventoryRequest(BaseSchema):
    # Catalog swagger.json

    
    item = fields.Nested(ItemQuery, required=False)
    
    sizes = fields.List(fields.Nested(InvSize, required=False), required=False)
    
    company_id = fields.Int(required=False)
    

