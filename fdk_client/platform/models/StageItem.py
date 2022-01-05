"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StageItem(BaseSchema):
    # Order swagger.json

    
    count = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

