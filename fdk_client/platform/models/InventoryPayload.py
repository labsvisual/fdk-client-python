"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class InventoryPayload(BaseSchema):
    # Catalog swagger.json

    
    seller_identifier = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    total_quantity = fields.Int(required=False)
    
    price_effective = fields.Float(required=False)
    
    expiration_date = fields.Str(required=False)
    
    price_marked = fields.Float(required=False)
    

