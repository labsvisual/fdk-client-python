"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Media import Media

from .AutocompleteAction import AutocompleteAction




class AutocompleteResult(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    

