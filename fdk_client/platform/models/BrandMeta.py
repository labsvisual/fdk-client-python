"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class BrandMeta(BaseSchema):
    # Catalog swagger.json

    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

