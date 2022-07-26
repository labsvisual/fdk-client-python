"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class DisplayMeta1(BaseSchema):
    # Cart swagger.json

    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    offer_text = fields.Str(required=False)
    

