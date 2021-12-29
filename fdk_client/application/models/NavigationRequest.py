"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Orientation import Orientation

from .NavigationReference import NavigationReference


class NavigationRequest(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    platform = fields.List(fields.Str(required=False), required=False)
    
    orientation = fields.Nested(Orientation, required=False)
    
    navigation = fields.List(fields.Nested(NavigationReference, required=False), required=False)
    

