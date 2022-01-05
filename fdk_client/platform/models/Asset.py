"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Asset(BaseSchema):
    # Content swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    

