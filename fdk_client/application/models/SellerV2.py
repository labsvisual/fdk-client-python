"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class SellerV2(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

