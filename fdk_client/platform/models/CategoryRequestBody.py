"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CategoryMapping import CategoryMapping



from .Hierarchy import Hierarchy











from .Media2 import Media2




class CategoryRequestBody(BaseSchema):
    # Catalog swagger.json

    
    priority = fields.Int(required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    name = fields.Str(required=False)
    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    level = fields.Int(required=False)
    

