"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class MetaStructure(BaseSchema):
    # Communication swagger.json

    
    job_type = fields.Str(required=False)
    
    action = fields.Str(required=False)
    
    trace = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    

