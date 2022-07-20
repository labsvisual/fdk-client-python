"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Locations(BaseSchema):
    # Configuration swagger.json

    
    items = fields.List(fields.Dict(required=False), required=False)
    

