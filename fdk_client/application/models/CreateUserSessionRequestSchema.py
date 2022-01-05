"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CreateUserSessionRequestSchema(BaseSchema):
    # User swagger.json

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    user_id = fields.Str(required=False)
    

