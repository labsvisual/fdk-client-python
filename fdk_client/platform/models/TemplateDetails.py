"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class TemplateDetails(BaseSchema):
    # Catalog swagger.json

    
    tag = fields.Str(required=False)
    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    departments = fields.List(fields.Str(required=False), required=False)
    
    is_expirable = fields.Boolean(required=False)
    
    is_physical = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    categories = fields.List(fields.Str(required=False), required=False)
    

