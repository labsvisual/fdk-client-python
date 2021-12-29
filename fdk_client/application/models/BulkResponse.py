"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CopyFileTask import CopyFileTask


class BulkResponse(BaseSchema):
    # FileStorage swagger.json

    
    tracking_url = fields.Str(required=False)
    
    task = fields.Nested(CopyFileTask, required=False)
    

