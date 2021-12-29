"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ScheduleStartSchema import ScheduleStartSchema


class AnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    announcement = fields.Str(required=False)
    
    schedule = fields.Nested(ScheduleStartSchema, required=False)
    

