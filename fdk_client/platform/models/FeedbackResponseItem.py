"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FeedbackResponseItem(BaseSchema):
    # Lead swagger.json

    
    display = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

