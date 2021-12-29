"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class AppliedFilters(BaseSchema):
    # Order swagger.json

    
    stage = fields.Str(required=False)
    
    stores = fields.List(fields.Str(required=False), required=False)
    
    deployment_stores = fields.List(fields.Str(required=False), required=False)
    
    dp = fields.List(fields.Int(required=False), required=False)
    
    from_date = fields.Str(required=False)
    
    to_date = fields.Str(required=False)
    

