"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ApikeyModel(BaseSchema):
    # Inventory swagger.json

    
    session_id = fields.Str(required=False)
    
    error_message = fields.Str(required=False)
    

