"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class ProductFiltersKey(BaseSchema):
    # Catalog swagger.json

    
    operators = fields.List(fields.Str(required=False), required=False)
    
    logo = fields.Str(required=False)
    
    display = fields.Str(required=False)
    
    kind = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

