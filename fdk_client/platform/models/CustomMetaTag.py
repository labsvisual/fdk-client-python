"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class CustomMetaTag(BaseSchema):
    # Content swagger.json

    
    name = fields.Str(required=False)
    
    content = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    

