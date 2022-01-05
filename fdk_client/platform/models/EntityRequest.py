"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class EntityRequest(BaseSchema):
    # Feedback swagger.json

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    

