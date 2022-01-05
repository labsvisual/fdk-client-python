"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class EditEmailRequestSchema(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    

