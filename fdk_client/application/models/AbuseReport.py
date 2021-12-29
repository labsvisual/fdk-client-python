"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DateMeta import DateMeta



from .Entity import Entity





from .FeedbackState import FeedbackState

from .TagMeta import TagMeta


class AbuseReport(BaseSchema):
    # Feedback swagger.json

    
    abused = fields.Boolean(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

