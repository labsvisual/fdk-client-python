"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .SegmentCredentials import SegmentCredentials




class Segment(BaseSchema):
    # Configuration swagger.json

    
    credentials = fields.Nested(SegmentCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

