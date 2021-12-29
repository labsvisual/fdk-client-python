"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class Language(BaseSchema):
    # Content swagger.json

    
    display = fields.Str(required=False)
    

