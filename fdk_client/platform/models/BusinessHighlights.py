"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class BusinessHighlights(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    

