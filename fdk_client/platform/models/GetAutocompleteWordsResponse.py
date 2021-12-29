"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetAutocompleteWordsData import GetAutocompleteWordsData

from .Page import Page


class GetAutocompleteWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetAutocompleteWordsData, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

