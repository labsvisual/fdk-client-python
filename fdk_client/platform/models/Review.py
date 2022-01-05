"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .MediaMeta import MediaMeta



from .MediaMeta import MediaMeta




class Review(BaseSchema):
    # Feedback swagger.json

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(MediaMeta, required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(MediaMeta, required=False)
    
    vote_allowed = fields.Boolean(required=False)
    

