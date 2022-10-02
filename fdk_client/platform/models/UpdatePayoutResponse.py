"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class UpdatePayoutResponse(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    success = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    

