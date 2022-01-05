"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Facebook(BaseSchema):
    # User swagger.json

    
    app_id = fields.Str(required=False)
    

