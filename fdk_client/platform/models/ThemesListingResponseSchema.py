"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ThemesSchema import ThemesSchema

from .PaginationSchema import PaginationSchema


class ThemesListingResponseSchema(BaseSchema):
    # Theme swagger.json

    
    items = fields.List(fields.Nested(ThemesSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

