"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .CompanyMeta import CompanyMeta



from .BrandMeta import BrandMeta



from .InventorySet import InventorySet





from .UserSerializer import UserSerializer



from .WeightResponse import WeightResponse

from .PriceMeta import PriceMeta

from .Quantities import Quantities



from .UserSerializer import UserSerializer





from .ManufacturerResponse import ManufacturerResponse

from .StoreMeta import StoreMeta





from .Trader1 import Trader1



from .ReturnConfig1 import ReturnConfig1











from .DimensionResponse import DimensionResponse


class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    fynd_item_code = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    country_of_origin = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    brand = fields.Nested(BrandMeta, required=False)
    
    stage = fields.Str(required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    fragile = fields.Boolean(required=False)
    
    is_set = fields.Boolean(required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    expiration_date = fields.Str(required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    item_id = fields.Int(required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    identifier = fields.Dict(required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    uid = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    total_quantity = fields.Int(required=False)
    
    meta = fields.Dict(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    

