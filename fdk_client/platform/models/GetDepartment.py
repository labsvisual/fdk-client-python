"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





















from .UserSerializer import UserSerializer

from .UserSerializer import UserSerializer








class GetDepartment(BaseSchema):
    # Catalog swagger.json

    
    page_no = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    modified_on = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    
    search = fields.Str(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    slug = fields.Str(required=False)
    
    page_size = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

