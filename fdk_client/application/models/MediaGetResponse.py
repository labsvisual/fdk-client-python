"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FeedbackMedia import FeedbackMedia

from .Page import Page


class MediaGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(FeedbackMedia, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

