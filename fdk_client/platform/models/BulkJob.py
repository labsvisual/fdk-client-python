"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .UserInfo1 import UserInfo1





























from .UserInfo1 import UserInfo1




class BulkJob(BaseSchema):
    # Catalog swagger.json

    
    modified_by = fields.Nested(UserInfo1, required=False)
    
    is_active = fields.Boolean(required=False)
    
    company_id = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    cancelled_records = fields.List(fields.Dict(required=False), required=False)
    
    modified_on = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    failed_records = fields.List(fields.Dict(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    custom_template_tag = fields.Str(required=False)
    
    tracking_url = fields.Str(required=False)
    
    created_by = fields.Nested(UserInfo1, required=False)
    
    created_on = fields.Str(required=False)
    

