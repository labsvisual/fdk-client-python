"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Comment import Comment

from .DateMeta import DateMeta

from .Entity import Entity





from .Question import Question

from .QNAState import QNAState



from .TagMeta import TagMeta


class QNA(BaseSchema):
    # Feedback swagger.json

    
    comments = fields.List(fields.Nested(Comment, required=False), required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    question = fields.Nested(Question, required=False)
    
    state = fields.Nested(QNAState, required=False)
    
    tag = fields.List(fields.Str(required=False), required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    

