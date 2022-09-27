"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
























class DepartmentCreateUpdate(BaseSchema):
    # Catalog swagger.json

    
    priority_order = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    _cls = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    platforms = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    

