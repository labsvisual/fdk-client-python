"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StoreDetail(BaseSchema):
    # Catalog swagger.json

    
    code = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    city = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

