"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class InventoryResponse(BaseSchema):
    # Catalog swagger.json

    
    quantity = fields.Int(required=False)
    
    seller_identifier = fields.Int(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    price_effective = fields.Int(required=False)
    
    price = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    identifiers = fields.Dict(required=False)
    
    currency = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    store = fields.Dict(required=False)
    
    price_transfer = fields.Int(required=False)
    

