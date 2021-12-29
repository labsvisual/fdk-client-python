"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AppStoreRules import AppStoreRules


class InventoryStore(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    stores = fields.List(fields.Raw(required=False), required=False)
    
    rules = fields.Nested(AppStoreRules, required=False)
    

