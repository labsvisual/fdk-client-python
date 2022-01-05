"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .BulkRequest import BulkRequest

from .Opts import Opts
















class CopyFileTask(BaseSchema):
    # FileStorage swagger.json

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    data = fields.Nested(BulkRequest, required=False)
    
    opts = fields.Nested(Opts, required=False)
    
    progress = fields.Int(required=False)
    
    delay = fields.Int(required=False)
    
    timestamp = fields.Int(required=False)
    
    attempts_made = fields.Int(required=False)
    
    stacktrace = fields.List(fields.Str(required=False), required=False)
    
    finished_on = fields.Int(required=False)
    
    processed_on = fields.Int(required=False)
    

