"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Gst import Gst


class Documents(BaseSchema):
    # Order swagger.json

    
    gst = fields.Nested(Gst, required=False)
    

