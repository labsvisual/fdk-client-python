"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AppStore import AppStore

from .Page import Page

from .StoreDepartments import StoreDepartments


class ApplicationStoreListing(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(AppStore, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    filters = fields.List(fields.Nested(StoreDepartments, required=False), required=False)
    

