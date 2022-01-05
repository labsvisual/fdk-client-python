"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Schedule import Schedule





from .Asset import Asset







from .ShareMessages import ShareMessages














class Offer(BaseSchema):
    # Rewards swagger.json

    
    _schedule = fields.Nested(Schedule, required=False)
    
    active = fields.Boolean(required=False)
    
    application_id = fields.Str(required=False)
    
    banner_image = fields.Nested(Asset, required=False)
    
    created_at = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    rule = fields.Dict(required=False)
    
    share = fields.Nested(ShareMessages, required=False)
    
    sub_text = fields.Str(required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    updated_by = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

