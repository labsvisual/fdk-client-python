"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .StoreMeta import StoreMeta



from .DimensionResponse import DimensionResponse

from .UserSerializer import UserSerializer

from .Quantities import Quantities



from .ReturnConfig1 import ReturnConfig1



from .Trader1 import Trader1



from .InventorySet import InventorySet









from .BrandMeta import BrandMeta

from .UserSerializer import UserSerializer









from .WeightResponse import WeightResponse







from .CompanyMeta import CompanyMeta







from .PriceMeta import PriceMeta

from .ManufacturerResponse import ManufacturerResponse






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    is_set = fields.Boolean(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    fragile = fields.Boolean(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    identifier = fields.Dict(required=False)
    
    added_on_store = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    

