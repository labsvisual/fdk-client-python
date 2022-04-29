"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Size(BaseSchema):
    # Catalog swagger.json

    
    is_available = fields.Boolean(required=False)
    
    display = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    value = fields.Str(required=False)
    

