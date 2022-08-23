"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class PriceMeta(BaseSchema):
    # Catalog swagger.json

    
    effective = fields.Float(required=False)
    
    transfer = fields.Float(required=False)
    
    tp_notes = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    marked = fields.Float(required=False)
    
    updated_at = fields.Str(required=False)
    

