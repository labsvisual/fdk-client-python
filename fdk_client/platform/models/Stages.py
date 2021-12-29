"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .StagesFilters import StagesFilters


class Stages(BaseSchema):
    # Order swagger.json

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    

