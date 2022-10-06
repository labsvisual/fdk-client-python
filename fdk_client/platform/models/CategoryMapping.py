"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues


class CategoryMapping(BaseSchema):
    # Catalog swagger.json

    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
    google = fields.Nested(CategoryMappingValues, required=False)
    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    

