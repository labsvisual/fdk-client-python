"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class JobLog(BaseSchema):
    # Communication swagger.json

    
    imported = fields.Raw(required=False)
    
    processed = fields.Raw(required=False)
    
    _id = fields.Str(required=False)
    
    job = fields.Str(required=False)
    
    campaign = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

