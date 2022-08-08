"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class OptInPostRequest(BaseSchema):
    # Catalog swagger.json

    
    opt_level = fields.Str(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    enabled = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    platform = fields.Str(required=False)
    

