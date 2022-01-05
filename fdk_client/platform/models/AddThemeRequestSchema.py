"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class AddThemeRequestSchema(BaseSchema):
    # Theme swagger.json

    
    theme_id = fields.Str(required=False)
    

