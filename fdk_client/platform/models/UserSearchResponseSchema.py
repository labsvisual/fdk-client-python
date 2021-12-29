"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserSchema import UserSchema


class UserSearchResponseSchema(BaseSchema):
    # User swagger.json

    
    users = fields.List(fields.Nested(UserSchema, required=False), required=False)
    

