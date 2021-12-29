"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FaqSchema import FaqSchema


class CreateFaqResponseSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FaqSchema, required=False)
    

