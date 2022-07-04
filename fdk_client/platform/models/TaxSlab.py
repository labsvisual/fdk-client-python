"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class TaxSlab(BaseSchema):
    # Catalog swagger.json

    
    threshold = fields.Float(required=False)
    
    cess = fields.Float(required=False)
    
    effective_date = fields.Str(required=False)
    
    rate = fields.Float(required=False)
    
