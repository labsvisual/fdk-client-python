"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class TaskParam(BaseSchema):
    # Inventory swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

