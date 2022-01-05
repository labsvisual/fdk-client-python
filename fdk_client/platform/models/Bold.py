"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Bold(BaseSchema):
    # Theme swagger.json

    
    name = fields.Str(required=False)
    
    file = fields.Str(required=False)
    

