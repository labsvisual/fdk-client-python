"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class UpdateDialog(BaseSchema):
    # Configuration swagger.json

    
    type = fields.Str(required=False)
    
    interval = fields.Int(required=False)
    

