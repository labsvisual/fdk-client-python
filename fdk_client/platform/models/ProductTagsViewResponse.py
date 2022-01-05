"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .NestedTags import NestedTags


class ProductTagsViewResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(NestedTags, required=False)
    

