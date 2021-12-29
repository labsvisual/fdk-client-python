"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AdminAnnouncementSchema import AdminAnnouncementSchema

from .Page import Page


class GetAnnouncementListSchema(BaseSchema):
    # Content swagger.json

    
    items = fields.List(fields.Nested(AdminAnnouncementSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

