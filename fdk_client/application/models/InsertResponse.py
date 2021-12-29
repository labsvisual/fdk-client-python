"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class InsertResponse(BaseSchema):
    # Feedback swagger.json

    
    ids = fields.Str(required=False)
    

