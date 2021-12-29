"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ReqConfiguration(BaseSchema):
    # FileStorage swagger.json

    
    concurrency = fields.Int(required=False)
    

