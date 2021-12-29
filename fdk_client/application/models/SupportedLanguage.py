"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SupportedLanguage(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

