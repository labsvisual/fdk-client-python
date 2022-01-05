"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .QNA import QNA

from .Page import Page


class QNAGetResponse(BaseSchema):
    # Feedback swagger.json

    
    items = fields.List(fields.Nested(QNA, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

