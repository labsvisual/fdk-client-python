"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Timestamp import Timestamp


class Promise(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(Timestamp, required=False)
    

