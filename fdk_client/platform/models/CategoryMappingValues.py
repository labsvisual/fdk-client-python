"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CategoryMappingValues(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    catalog_id = fields.Int(required=False)
    

