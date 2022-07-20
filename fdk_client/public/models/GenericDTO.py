"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class GenericDTO(BaseSchema):
    # Inventory swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

