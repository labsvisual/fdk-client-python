"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ApplicationSchema import ApplicationSchema

from .Cloud import Cloud

from .CreatedBy import CreatedBy

from .DateMeta import DateMeta



from .Entity import Entity





from .Entity import Entity

from .MediaState import MediaState

from .TagMeta import TagMeta



from .Url import Url


class FeedbackMedia(BaseSchema):
    # Feedback swagger.json

    
    application = fields.Nested(ApplicationSchema, required=False)
    
    cloud = fields.Nested(Cloud, required=False)
    
    created_by = fields.Nested(CreatedBy, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    description = fields.Str(required=False)
    
    entity = fields.Nested(Entity, required=False)
    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    reference = fields.Nested(Entity, required=False)
    
    state = fields.Nested(MediaState, required=False)
    
    tags = fields.List(fields.Nested(TagMeta, required=False), required=False)
    
    type = fields.Str(required=False)
    
    url = fields.Nested(Url, required=False)
    

