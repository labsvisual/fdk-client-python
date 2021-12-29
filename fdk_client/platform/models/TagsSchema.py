"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .TagSchema import TagSchema


class TagsSchema(BaseSchema):
    # Content swagger.json

    
    application = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagSchema, required=False), required=False)
    

