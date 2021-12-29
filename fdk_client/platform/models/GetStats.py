"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Stats import Stats


class GetStats(BaseSchema):
    # Communication swagger.json

    
    items = fields.List(fields.Nested(Stats, required=False), required=False)
    

