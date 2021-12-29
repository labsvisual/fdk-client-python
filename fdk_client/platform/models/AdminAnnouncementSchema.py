"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AnnouncementPageSchema import AnnouncementPageSchema

from .EditorMeta import EditorMeta

from .AnnouncementAuthorSchema import AnnouncementAuthorSchema







from .ScheduleSchema import ScheduleSchema


class AdminAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    _id = fields.Str(required=False)
    
    platforms = fields.List(fields.Str(required=False), required=False)
    
    title = fields.Str(required=False)
    
    announcement = fields.Str(required=False)
    
    pages = fields.List(fields.Nested(AnnouncementPageSchema, required=False), required=False)
    
    editor_meta = fields.Nested(EditorMeta, required=False)
    
    author = fields.Nested(AnnouncementAuthorSchema, required=False)
    
    created_at = fields.Str(required=False)
    
    app = fields.Str(required=False)
    
    modified_at = fields.Str(required=False)
    
    _schedule = fields.Nested(ScheduleSchema, required=False)
    

