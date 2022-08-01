"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class QuantityBase(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    

