"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .AutocompletePageAction import AutocompletePageAction




class AutocompleteAction(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(AutocompletePageAction, required=False)
    
    type = fields.Str(required=False)
    

