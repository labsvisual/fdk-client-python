"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .CategoryMapping import CategoryMapping





from .Media2 import Media2















from .Hierarchy import Hierarchy








class Category(BaseSchema):
    # Catalog swagger.json

    
    modified_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    level = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    priority = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    modified_by = fields.Dict(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    

