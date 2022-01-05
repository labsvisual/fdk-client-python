"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .TextDetector import TextDetector


class AutoDetectors(BaseSchema):
    # Feedback swagger.json

    
    text_detector = fields.List(fields.Nested(TextDetector, required=False), required=False)
    

