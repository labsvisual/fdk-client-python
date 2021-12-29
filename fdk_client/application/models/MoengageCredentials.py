"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class MoengageCredentials(BaseSchema):
    # Configuration swagger.json

    
    app_id = fields.Str(required=False)
    

