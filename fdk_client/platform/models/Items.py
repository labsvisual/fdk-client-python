"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .UserCommon import UserCommon

























from .UserCommon import UserCommon


class Items(BaseSchema):
    # Catalog swagger.json

    
    tracking_url = fields.Str(required=False)
    
    failed = fields.Int(required=False)
    
    id = fields.Str(required=False)
    
    created_by = fields.Nested(UserCommon, required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    retry = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    
    total = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    file_path = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    cancelled = fields.Int(required=False)
    
    modified_by = fields.Nested(UserCommon, required=False)
    

