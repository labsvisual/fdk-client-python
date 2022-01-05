"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class Colors(BaseSchema):
    # Theme swagger.json

    
    bg_color = fields.Str(required=False)
    
    primary_color = fields.Str(required=False)
    
    secondary_color = fields.Str(required=False)
    
    accent_color = fields.Str(required=False)
    
    link_color = fields.Str(required=False)
    
    button_secondary_color = fields.Str(required=False)
    

