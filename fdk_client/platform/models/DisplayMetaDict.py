"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DisplayMetaDict(BaseSchema):
    # Cart swagger.json

    
    subtitle = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

