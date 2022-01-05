"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FAQ import FAQ


class CreateFaqSchema(BaseSchema):
    # Content swagger.json

    
    faq = fields.Nested(FAQ, required=False)
    

