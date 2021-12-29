"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AdminAnnouncementSchema import AdminAnnouncementSchema


class CreateAnnouncementSchema(BaseSchema):
    # Content swagger.json

    
    message = fields.Str(required=False)
    
    data = fields.Nested(AdminAnnouncementSchema, required=False)
    

