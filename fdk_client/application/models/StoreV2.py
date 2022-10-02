"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class StoreV2(BaseSchema):
    # Catalog swagger.json

    
    name = fields.Str(required=False)
    
    count = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    

