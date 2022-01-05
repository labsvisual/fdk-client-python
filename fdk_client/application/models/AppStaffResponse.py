"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppStaff import AppStaff


class AppStaffResponse(BaseSchema):
    # Configuration swagger.json

    
    staff_users = fields.List(fields.Nested(AppStaff, required=False), required=False)
    

