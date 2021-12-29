"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AddMediaRequest import AddMediaRequest






class AddMediaListRequest(BaseSchema):
    # Feedback swagger.json

    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_list = fields.List(fields.Nested(AddMediaRequest, required=False), required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

