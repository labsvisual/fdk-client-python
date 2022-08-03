"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class StrategyWiseListingSchemaV2(BaseSchema):
    # Catalog swagger.json

    
    distance = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    tat = fields.Int(required=False)
    
    pincode = fields.Int(required=False)
    

