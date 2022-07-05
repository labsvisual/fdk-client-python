"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Validation(BaseSchema):
    # Cart swagger.json

    
    user_registered_after = fields.Str(required=False)
    
    app_id = fields.List(fields.Str(required=False), required=False)
    
    anonymous = fields.Boolean(required=False)
    

