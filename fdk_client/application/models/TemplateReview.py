"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ReviewMediaMeta import ReviewMediaMeta



from .ReviewMediaMeta import ReviewMediaMeta




class TemplateReview(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(ReviewMediaMeta, required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(ReviewMediaMeta, required=False)
    
    vote_allowed = fields.Boolean(required=False)
    

