"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class OptInPostRequest(BaseSchema):
    # Catalog swagger.json

    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    enabled = fields.Boolean(required=False)
    
    opt_level = fields.Str(required=False)
    

