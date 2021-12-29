"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UrlInfo(BaseSchema):
    # Share swagger.json

    
    original = fields.Str(required=False)
    
    short = fields.Str(required=False)
    
    hash = fields.Str(required=False)
    

