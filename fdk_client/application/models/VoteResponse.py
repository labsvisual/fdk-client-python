"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Vote import Vote

from .Page import Page


class VoteResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(Vote, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

