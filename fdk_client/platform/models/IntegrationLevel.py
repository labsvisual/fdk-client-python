"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .LastPatch import LastPatch









from .IntegrationMeta import IntegrationMeta












class IntegrationLevel(BaseSchema):
    # Configuration swagger.json

    
    opted = fields.Boolean(required=False)
    
    permissions = fields.List(fields.Dict(required=False), required=False)
    
    last_patch = fields.List(fields.Nested(LastPatch, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    integration = fields.Str(required=False)
    
    level = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    meta = fields.List(fields.Nested(IntegrationMeta, required=False), required=False)
    
    token = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    
    data = fields.Dict(required=False)
    

