"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class DeploymentStoreSelectionFeature(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

