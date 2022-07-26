"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class StoreDepartments(BaseSchema):
    # Catalog swagger.json

    
    slug = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    priority_order = fields.Int(required=False)
    

