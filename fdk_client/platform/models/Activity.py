"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Activity(BaseSchema):
    # Feedback swagger.json

    
    current_state = fields.Dict(required=False)
    
    document_id = fields.Str(required=False)
    
    previous_state = fields.Dict(required=False)
    

