"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class AddMediaRequest(BaseSchema):
    # Feedback swagger.json

    
    cloud_id = fields.Str(required=False)
    
    cloud_name = fields.Str(required=False)
    
    cloud_provider = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_url = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    thumbnail_url = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

