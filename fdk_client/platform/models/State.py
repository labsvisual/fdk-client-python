"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class State(BaseSchema):
    # Cart swagger.json

    
    is_archived = fields.Boolean(required=False)
    
    is_display = fields.Boolean(required=False)
    
    is_public = fields.Boolean(required=False)
    

