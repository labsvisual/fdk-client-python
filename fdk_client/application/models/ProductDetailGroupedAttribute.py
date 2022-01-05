"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductDetailAttribute import ProductDetailAttribute


class ProductDetailGroupedAttribute(BaseSchema):
    # Catalog swagger.json

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(ProductDetailAttribute, required=False), required=False)
    

