"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DateMeta import DateMeta

from .Entity import Entity





from .Rating import Rating

from .Review import Review

from .FeedbackState import FeedbackState

from .TagMeta import TagMeta


class Template(BaseSchema):
    # Feedback swagger.json

    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rating = fields.Nested(Rating, required=False)
    
    review = fields.Nested(Review, required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

