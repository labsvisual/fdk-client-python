"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UpdateCommentRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    comment = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    

