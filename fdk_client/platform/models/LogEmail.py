"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class LogEmail(BaseSchema):
    # Communication swagger.json

    
    template = fields.Str(required=False)
    

