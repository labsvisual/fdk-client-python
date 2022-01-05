"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FAQ(BaseSchema):
    # Content swagger.json

    
    slug = fields.Str(required=False)
    
    question = fields.Str(required=False)
    
    answer = fields.Str(required=False)
    

