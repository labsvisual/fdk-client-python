"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetSearchWordsData import GetSearchWordsData

from .Page import Page


class GetSearchWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetSearchWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

