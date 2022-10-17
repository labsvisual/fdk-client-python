"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Price1 import Price1

from .Price1 import Price1


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    marked = fields.Nested(Price1, required=False)
    
    effective = fields.Nested(Price1, required=False)
    

