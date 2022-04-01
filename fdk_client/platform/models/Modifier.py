"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Modifier(BaseSchema):
    # AuditTrail swagger.json

    
    user_id = fields.Str(required=False)
    
    as_administrator = fields.Boolean(required=False)
    
    user_details = fields.Dict(required=False)
    

