"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Logo(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    aspect_ratio_f = fields.Int(required=False)
    
    secure_url = fields.Str(required=False)
    
    aspect_ratio = fields.Str(required=False)
    

