"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class PromotionSchedule(BaseSchema):
    # Cart swagger.json

    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    published = fields.Boolean(required=False)
    
    cron = fields.Str(required=False)
    

