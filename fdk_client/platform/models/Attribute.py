"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DateMeta import DateMeta









from .TagMeta import TagMeta


class Attribute(BaseSchema):
    # Feedback swagger.json

    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

