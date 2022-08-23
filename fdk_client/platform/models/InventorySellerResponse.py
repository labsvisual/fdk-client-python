"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .BrandMeta import BrandMeta

from .WeightResponse import WeightResponse

from .InventorySet import InventorySet



from .DimensionResponse import DimensionResponse







from .StoreMeta import StoreMeta











from .PriceMeta import PriceMeta







from .ReturnConfig1 import ReturnConfig1

from .UserSerializer import UserSerializer





from .CompanyMeta import CompanyMeta



from .ManufacturerResponse import ManufacturerResponse

from .UserSerializer import UserSerializer

from .Trader1 import Trader1









from .Quantities import Quantities






class InventorySellerResponse(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.Nested(BrandMeta, required=False)
    
    weight = fields.Nested(WeightResponse, required=False)
    
    set = fields.Nested(InventorySet, required=False)
    
    country_of_origin = fields.Str(required=False)
    
    dimension = fields.Nested(DimensionResponse, required=False)
    
    fynd_article_code = fields.Str(required=False)
    
    fynd_item_code = fields.Str(required=False)
    
    fynd_meta = fields.Dict(required=False)
    
    store = fields.Nested(StoreMeta, required=False)
    
    size = fields.Str(required=False)
    
    track_inventory = fields.Boolean(required=False)
    
    fragile = fields.Boolean(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(PriceMeta, required=False)
    
    meta = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    added_on_store = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig1, required=False)
    
    modified_by = fields.Nested(UserSerializer, required=False)
    
    raw_meta = fields.Dict(required=False)
    
    expiration_date = fields.Str(required=False)
    
    company = fields.Nested(CompanyMeta, required=False)
    
    stage = fields.Str(required=False)
    
    manufacturer = fields.Nested(ManufacturerResponse, required=False)
    
    created_by = fields.Nested(UserSerializer, required=False)
    
    trader = fields.List(fields.Nested(Trader1, required=False), required=False)
    
    identifier = fields.Dict(required=False)
    
    is_set = fields.Boolean(required=False)
    
    uid = fields.Str(required=False)
    
    _custom_json = fields.Dict(required=False)
    
    quantities = fields.Nested(Quantities, required=False)
    
    tax_identifier = fields.Dict(required=False)
    
    total_quantity = fields.Int(required=False)
    

