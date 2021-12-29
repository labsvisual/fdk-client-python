"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .EntityRequest import EntityRequest

from .RatingRequest import RatingRequest

from .ReviewRequest import ReviewRequest


class UpdateTemplateRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    enable_media_type = fields.Str(required=False)
    
    enable_qna = fields.Boolean(required=False)
    
    enable_rating = fields.Boolean(required=False)
    
    enable_review = fields.Boolean(required=False)
    
    entity = fields.Nested(EntityRequest, required=False)
    
    rating = fields.Nested(RatingRequest, required=False)
    
    review = fields.Nested(ReviewRequest, required=False)
    

