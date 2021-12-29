"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SortMethod(BaseSchema):
    # Feedback swagger.json

    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

