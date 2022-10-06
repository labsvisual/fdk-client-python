"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .NextSchedule import NextSchedule










class CollectionSchedule(BaseSchema):
    # Catalog swagger.json

    
    next_schedule = fields.List(fields.Nested(NextSchedule, required=False), required=False)
    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    

