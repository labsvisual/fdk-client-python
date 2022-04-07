"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .UserDetail import UserDetail

from .UserDetail import UserDetail







from .ProductTemplate import ProductTemplate




class ProductBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    total = fields.Int(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    cancelled = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    failed = fields.Int(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    stage = fields.Str(required=False)
    

