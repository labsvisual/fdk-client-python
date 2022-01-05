"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class DeploymentMeta(BaseSchema):
    # Configuration swagger.json

    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    all_stores = fields.Boolean(required=False)
    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    app = fields.Str(required=False)
    

