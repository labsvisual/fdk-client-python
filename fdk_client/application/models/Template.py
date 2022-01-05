"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DateMeta import DateMeta

from .Entity import Entity





from .Rating import Rating

from .TemplateReview import TemplateReview

from .FeedbackState import FeedbackState


class Template(BaseSchema):
    # Feedback swagger.json

    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Nested(Rating, required=False)
    
    review = fields.Nested(TemplateReview, required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    

