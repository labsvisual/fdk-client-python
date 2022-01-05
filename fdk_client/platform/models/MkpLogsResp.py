"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class MkpLogsResp(BaseSchema):
    # Analytics swagger.json

    
    start_time_iso = fields.Str(required=False)
    
    end_time_iso = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    count = fields.Str(required=False)
    
    status = fields.Str(required=False)
    

