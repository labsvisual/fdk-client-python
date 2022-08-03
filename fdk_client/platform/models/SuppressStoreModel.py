"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SuppressStoreModel(BaseSchema):
    # Inventory swagger.json

    
    stores = fields.List(fields.Int(required=False), required=False)
    

