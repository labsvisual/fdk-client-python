"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    store_type = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    store_code = fields.Str(required=False)
    
    display_name = fields.Str(required=False)
    
    timing = fields.Dict(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    name = fields.Str(required=False)
    

