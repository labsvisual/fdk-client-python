"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class BlockUserRequestSchema(BaseSchema):
    # User swagger.json

    
    status = fields.Boolean(required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Str(required=False)
    

