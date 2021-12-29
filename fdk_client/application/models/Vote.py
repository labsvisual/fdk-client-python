"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .DateMeta import DateMeta

from .Entity import Entity





from .Entity import Entity

from .FeedbackState import FeedbackState

from .TagMeta import TagMeta


class Vote(BaseSchema):
    # Feedback swagger.json

    
    action = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    reference = fields.Nested(Entity, required=False)
    
    state = fields.Nested(FeedbackState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

