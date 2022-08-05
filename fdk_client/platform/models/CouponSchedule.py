"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class CouponSchedule(BaseSchema):
    # Cart swagger.json

    
    cron = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    end = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    

