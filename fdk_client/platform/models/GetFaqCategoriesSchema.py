"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CategorySchema import CategorySchema


class GetFaqCategoriesSchema(BaseSchema):
    # Content swagger.json

    
    categories = fields.List(fields.Nested(CategorySchema, required=False), required=False)
    

