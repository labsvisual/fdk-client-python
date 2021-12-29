"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .HandpickedTagSchema import HandpickedTagSchema


class UpdateHandpickedSchema(BaseSchema):
    # Content swagger.json

    
    tag = fields.Nested(HandpickedTagSchema, required=False)
    

