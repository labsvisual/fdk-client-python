"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OS(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

