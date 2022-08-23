"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductImage(BaseSchema):
    # Cart swagger.json

    
    aspect_ratio = fields.Str(required=False)
    
    secure_url = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

