"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Options import Options


class StagesFilters(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    options = fields.Nested(Options, required=False)
    

