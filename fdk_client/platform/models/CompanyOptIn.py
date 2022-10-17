"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






















class CompanyOptIn(BaseSchema):
    # Catalog swagger.json

    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    modified_by = fields.Dict(required=False)
    
    opt_level = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    modified_on = fields.Int(required=False)
    
    created_on = fields.Int(required=False)
    
    platform = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

