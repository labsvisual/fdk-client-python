"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Identifiers(BaseSchema):
    # Order swagger.json

    
    ean = fields.Str(required=False)
    
    sku_code = fields.Str(required=False)
    

