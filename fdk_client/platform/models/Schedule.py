"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .NextSchedule import NextSchedule


class Schedule(BaseSchema):
    # Catalog swagger.json

    
    duration = fields.Int(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    cron = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    

