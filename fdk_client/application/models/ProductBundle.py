"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .GetGroupedProducts import GetGroupedProducts


class ProductBundle(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetGroupedProducts, required=False), required=False)
    

