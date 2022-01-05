"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UpdateResponse(BaseSchema):
    # Feedback swagger.json

    
    id = fields.Str(required=False)
    

