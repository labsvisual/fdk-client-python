"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ActionPage import ActionPage

from .ActionPage import ActionPage




class Action(BaseSchema):
    # Content swagger.json

    
    page = fields.Nested(ActionPage, required=False)
    
    popup = fields.Nested(ActionPage, required=False)
    
    type = fields.Str(required=False)
    

