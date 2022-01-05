"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Entity(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

