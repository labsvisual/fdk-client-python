"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

