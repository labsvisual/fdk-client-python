"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StatsProcessedSms(BaseSchema):
    # Communication swagger.json

    
    success = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    suppressed = fields.Int(required=False)
    

