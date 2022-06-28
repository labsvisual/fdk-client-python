"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class TaxSlab(BaseSchema):
    # Catalog swagger.json

    
    effective_date = fields.Str(required=False)
    
    threshold = fields.Float(required=False)
    
    cess = fields.Float(required=False)
    
    rate = fields.Float(required=False)
    

