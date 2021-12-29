"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Links(BaseSchema):
    # Configuration swagger.json

    
    title = fields.Str(required=False)
    
    link = fields.Str(required=False)
    

