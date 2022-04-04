"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Media2(BaseSchema):
    # Catalog swagger.json

    
    logo = fields.Str(required=False)
    
    portrait = fields.Str(required=False)
    
    landscape = fields.Str(required=False)
    

