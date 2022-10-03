"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Properties import Properties








class GlobalValidation(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    properties = fields.Nested(Properties, required=False)
    
    description = fields.Str(required=False)
    
    required = fields.List(fields.Str(required=False), required=False)
    
    definitions = fields.Dict(required=False)
    

