"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CreateTagSchema import CreateTagSchema


class CreateTagRequestSchema(BaseSchema):
    # Content swagger.json

    
    tags = fields.List(fields.Nested(CreateTagSchema, required=False), required=False)
    

