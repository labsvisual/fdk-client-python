"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Preset import Preset

from .GlobalSchema import GlobalSchema



from .ListSchemaItem import ListSchemaItem


class Config(BaseSchema):
    # Theme swagger.json

    
    preset = fields.Nested(Preset, required=False)
    
    global_schema = fields.Nested(GlobalSchema, required=False)
    
    current = fields.Str(required=False)
    
    list = fields.List(fields.Nested(ListSchemaItem, required=False), required=False)
    

