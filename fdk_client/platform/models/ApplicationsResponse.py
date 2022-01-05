"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Application import Application

from .Page import Page


class ApplicationsResponse(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Nested(Application, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

