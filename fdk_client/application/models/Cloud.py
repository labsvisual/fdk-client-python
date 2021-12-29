"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Cloud(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    

