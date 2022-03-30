"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .AppStaff import AppStaff


class AppStaffListResponse(BaseSchema):
    # Configuration swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(AppStaff, required=False), required=False)
    

