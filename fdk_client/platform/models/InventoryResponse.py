"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class InventoryResponse(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    price_effective = fields.Float(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    store = fields.Dict(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price_transfer = fields.Float(required=False)
    
    price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    identifiers = fields.Dict(required=False)
    

