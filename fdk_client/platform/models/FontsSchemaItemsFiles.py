"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FontsSchemaItemsFiles(BaseSchema):
    # Theme swagger.json

    
    regular = fields.Str(required=False)
    
    italic = fields.Str(required=False)
    
    bold = fields.Str(required=False)
    

