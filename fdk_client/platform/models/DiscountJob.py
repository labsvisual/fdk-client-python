"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

























from .ValidityObject import ValidityObject





from .UserDetails import UserDetails

from .UserDetails import UserDetails




class DiscountJob(BaseSchema):
    # Discount swagger.json

    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    app_ids = fields.List(fields.Str(required=False), required=False)
    
    job_type = fields.Str(required=False)
    
    discount_type = fields.Str(required=False)
    
    discount_level = fields.Str(required=False)
    
    value = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    validity = fields.Nested(ValidityObject, required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_by = fields.Nested(UserDetails, required=False)
    
    modified_by = fields.Nested(UserDetails, required=False)
    
    meta = fields.Dict(required=False)
    

