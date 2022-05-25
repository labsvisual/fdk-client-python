"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Css(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    
    links = fields.List(fields.Str(required=False), required=False)
    

