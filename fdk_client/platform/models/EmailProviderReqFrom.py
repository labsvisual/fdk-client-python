"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class EmailProviderReqFrom(BaseSchema):
    # Communication swagger.json

    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    

