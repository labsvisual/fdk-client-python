"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Log import Log

from .Page import Page


class Logs(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Log, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

