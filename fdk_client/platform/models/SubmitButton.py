"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SubmitButton(BaseSchema):
    # Lead swagger.json

    
    title = fields.Str(required=False)
    
    title_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    

