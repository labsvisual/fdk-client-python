"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Rating import Rating

from .Page import Page


class RatingGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Rating, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

