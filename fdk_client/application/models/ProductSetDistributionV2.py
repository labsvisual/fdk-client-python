"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSetDistributionSizeV2 import ProductSetDistributionSizeV2


class ProductSetDistributionV2(BaseSchema):
    # Catalog swagger.json

    
    sizes = fields.List(fields.Nested(ProductSetDistributionSizeV2, required=False), required=False)
    

