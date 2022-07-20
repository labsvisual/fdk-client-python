"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class EmailJobMetrics(BaseSchema):
    # Inventory swagger.json

    
    executed = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    job_code = fields.Str(required=False)
    
    daily_job = fields.Boolean(required=False)
    
    last_executed_on = fields.Str(required=False)
    

