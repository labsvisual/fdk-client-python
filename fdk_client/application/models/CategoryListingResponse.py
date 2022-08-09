"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DepartmentIdentifier import DepartmentIdentifier

from .DepartmentCategoryTree import DepartmentCategoryTree


class CategoryListingResponse(BaseSchema):
    # Catalog swagger.json

    
    departments = fields.List(fields.Nested(DepartmentIdentifier, required=False), required=False)
    
    data = fields.List(fields.Nested(DepartmentCategoryTree, required=False), required=False)
    

