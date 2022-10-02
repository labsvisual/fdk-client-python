"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Page import Page

from .AppStore import AppStore

from .StoreDepartments import StoreDepartments


class ApplicationStoreListing(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    

