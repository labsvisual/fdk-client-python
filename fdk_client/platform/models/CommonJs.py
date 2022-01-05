"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class CommonJs(BaseSchema):
    # Theme swagger.json

    
    link = fields.Str(required=False)
    

