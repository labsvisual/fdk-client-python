"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CategoryItems import CategoryItems




class DepartmentCategoryTree(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(CategoryItems, required=False), required=False)
    
    department = fields.Str(required=False)
    

