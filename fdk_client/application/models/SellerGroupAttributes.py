"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .DetailsSchemaV2 import DetailsSchemaV2




class SellerGroupAttributes(BaseSchema):
    # Catalog swagger.json

    
    details = fields.List(fields.Nested(DetailsSchemaV2, required=False), required=False)
    
    title = fields.Str(required=False)
    

