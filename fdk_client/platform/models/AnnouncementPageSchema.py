"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class AnnouncementPageSchema(BaseSchema):
    # Content swagger.json

    
    page_slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

