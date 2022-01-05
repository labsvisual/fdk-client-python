"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ApplicationSchema(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    

