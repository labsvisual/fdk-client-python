"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class UpdateMediaListRequest(BaseSchema):
    # Feedback swagger.json

    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    ids = fields.List(fields.Str(required=False), required=False)
    

