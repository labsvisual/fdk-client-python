"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .CategorySchema import CategorySchema


class UpdateFaqCategoryRequestSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(CategorySchema, required=False)
    

