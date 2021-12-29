"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PlatformMobile(BaseSchema):
    # User swagger.json

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    

