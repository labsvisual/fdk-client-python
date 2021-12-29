"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSchema import UserSchema

from .PaginationSchema import PaginationSchema


class CustomerListResponseSchema(BaseSchema):
    # User swagger.json

    
    items = fields.List(fields.Nested(UserSchema, required=False), required=False)
    
    page = fields.Nested(PaginationSchema, required=False)
    

