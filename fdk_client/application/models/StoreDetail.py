"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    city = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

