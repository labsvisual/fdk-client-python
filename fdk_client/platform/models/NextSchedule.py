"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class NextSchedule(BaseSchema):
    # Content swagger.json

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    

