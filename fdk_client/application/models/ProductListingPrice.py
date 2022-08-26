"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Price import Price

from .Price import Price


class ProductListingPrice(BaseSchema):
    # Catalog swagger.json

    
    marked = fields.Nested(Price, required=False)
    
    effective = fields.Nested(Price, required=False)
    

