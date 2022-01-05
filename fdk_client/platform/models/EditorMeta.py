"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class EditorMeta(BaseSchema):
    # Content swagger.json

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    

