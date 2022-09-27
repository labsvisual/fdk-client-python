"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SizeDistribution import SizeDistribution




class InventorySet(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    
    quantity = fields.Int(required=False)
    

