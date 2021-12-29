"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Category import Category


class SingleCategoryResponse(BaseSchema):
    # Catalog swagger.json

    
    data = fields.Nested(Category, required=False)
    

