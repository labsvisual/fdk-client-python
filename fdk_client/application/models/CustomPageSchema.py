"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .CreatedBySchema import CreatedBySchema

from .DateMeta import DateMeta

from .ScheduleSchema import ScheduleSchema


class CustomPageSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    orientation = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    content = fields.List(fields.Dict(required=False), required=False)
    
    created_by = fields.Nested(CreatedBySchema, required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    

