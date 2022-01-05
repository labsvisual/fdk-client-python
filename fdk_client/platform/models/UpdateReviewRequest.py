"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .AttributeObject import AttributeObject



from .DeviceMeta import DeviceMeta





from .MediaMeta import MediaMeta










class UpdateReviewRequest(BaseSchema):
    # Feedback swagger.json

    
    active = fields.Boolean(required=False)
    
    application = fields.Str(required=False)
    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    attributes_rating = fields.List(fields.Nested(AttributeObject, required=False), required=False)
    
    description = fields.Str(required=False)
    
    device_meta = fields.Nested(DeviceMeta, required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    media_resource = fields.List(fields.Nested(MediaMeta, required=False), required=False)
    
    rating = fields.Float(required=False)
    
    review_id = fields.Str(required=False)
    
    template_id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

