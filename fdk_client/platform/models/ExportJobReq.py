"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ExportJobReq(BaseSchema):
    # Analytics swagger.json

    
    marketplace_name = fields.Str(required=False)
    
    start_time = fields.Str(required=False)
    
    end_time = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    

