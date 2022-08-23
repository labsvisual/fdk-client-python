"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetDepartment import GetDepartment

from .Page import Page


class DepartmentsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetDepartment, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

