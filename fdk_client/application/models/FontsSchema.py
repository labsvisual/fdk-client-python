"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FontsSchemaItems import FontsSchemaItems




class FontsSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.Nested(FontsSchemaItems, required=False)
    
    kind = fields.Str(required=False)
    

