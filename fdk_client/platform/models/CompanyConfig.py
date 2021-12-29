"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CompanyConfig(BaseSchema):
    # Inventory swagger.json

    
    company_id = fields.Int(required=False)
    
    exclude_steps = fields.List(fields.Int(required=False), required=False)
    
    hidden_closet_keys = fields.List(fields.Str(required=False), required=False)
    
    open_tags = fields.Dict(required=False)
    
    tax_identifiers = fields.List(fields.Str(required=False), required=False)
    
    delete_quantity_threshold = fields.Int(required=False)
    

