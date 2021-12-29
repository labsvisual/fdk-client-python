"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .FAQCategorySchema import FAQCategorySchema


class GetFaqCategoryBySlugSchema(BaseSchema):
    # Content swagger.json

    
    category = fields.Nested(FAQCategorySchema, required=False)
    

