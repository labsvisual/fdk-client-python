"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UIIcon(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Str(required=False)
    
    inactive = fields.Str(required=False)
    
    selected = fields.List(fields.Str(required=False), required=False)
    

