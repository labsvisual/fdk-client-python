"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class ConfigurationSchema(BaseSchema):
    # Content swagger.json

    
    sleep_time = fields.Int(required=False)
    
    start_on_launch = fields.Boolean(required=False)
    
    duration = fields.Int(required=False)
    
    slide_direction = fields.Str(required=False)
    

