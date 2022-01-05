"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class SessionListSuccess(BaseSchema):
    # User swagger.json

    
    sessions = fields.List(fields.Str(required=False), required=False)
    

