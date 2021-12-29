"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .StoreCriteriaRule import StoreCriteriaRule




class InventoryStoreRule(BaseSchema):
    # Configuration swagger.json

    
    criteria = fields.Str(required=False)
    
    rules = fields.List(fields.Nested(StoreCriteriaRule, required=False), required=False)
    
    stores = fields.List(fields.Int(required=False), required=False)
    

