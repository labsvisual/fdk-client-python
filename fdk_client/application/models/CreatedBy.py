"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .TagMeta import TagMeta


class CreatedBy(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

