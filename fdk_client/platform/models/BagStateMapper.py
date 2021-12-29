"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class BagStateMapper(BaseSchema):
    # Order swagger.json

    
    app_state_name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    display_name = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    app_display_name = fields.Str(required=False)
    

