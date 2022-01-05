"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema















from .JobMetricsDto import JobMetricsDto

from .JobMetricsDto import JobMetricsDto



from .Page import Page


class ResponseEnvelopeJobMetricsDto(BaseSchema):
    # Inventory swagger.json

    
    timestamp = fields.Str(required=False)
    
    status = fields.Int(required=False)
    
    error = fields.Str(required=False)
    
    exception = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    total_time_taken_in_millis = fields.Int(required=False)
    
    http_status = fields.Str(required=False)
    
    items = fields.Nested(JobMetricsDto, required=False)
    
    payload = fields.Nested(JobMetricsDto, required=False)
    
    trace_id = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    

