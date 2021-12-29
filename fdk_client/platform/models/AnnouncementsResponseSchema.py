"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class AnnouncementsResponseSchema(BaseSchema):
    # Content swagger.json

    
    announcements = fields.Dict(required=False)
    
    refresh_rate = fields.Int(required=False)
    
    refresh_pages = fields.List(fields.Str(required=False), required=False)
    

