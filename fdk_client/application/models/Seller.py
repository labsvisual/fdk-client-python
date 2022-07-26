"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class Seller(BaseSchema):
    # Catalog swagger.json

    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

