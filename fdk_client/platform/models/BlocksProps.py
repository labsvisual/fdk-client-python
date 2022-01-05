"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class BlocksProps(BaseSchema):
    # Theme swagger.json

    
    id = fields.Str(required=False)
    
    label = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

