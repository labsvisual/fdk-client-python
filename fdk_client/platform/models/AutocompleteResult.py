"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AutocompleteAction import AutocompleteAction

from .Media import Media




class AutocompleteResult(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    

