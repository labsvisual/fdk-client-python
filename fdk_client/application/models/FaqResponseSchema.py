"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FaqSchema import FaqSchema


class FaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faqs = fields.List(fields.Nested(FaqSchema, required=False), required=False)
    

