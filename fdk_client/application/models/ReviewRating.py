"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AttributeObject import AttributeObject




class ReviewRating(BaseSchema):
    # Feedback swagger.json

    
    attributes = fields.List(fields.Nested(AttributeObject, required=False), required=False)
    
    value = fields.Float(required=False)
    

