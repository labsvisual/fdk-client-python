"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class FilterOrderingStoreRequest(BaseSchema):
    # Configuration swagger.json

    
    all_stores = fields.Boolean(required=False)
    
    deployed_stores = fields.List(fields.Int(required=False), required=False)
    
    q = fields.Str(required=False)
    

