"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .OptType import OptType




class OptedInventory(BaseSchema):
    # Configuration swagger.json

    
    opt_type = fields.Nested(OptType, required=False)
    
    items = fields.Raw(required=False)
    

