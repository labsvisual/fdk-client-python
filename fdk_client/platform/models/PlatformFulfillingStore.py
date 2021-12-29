"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .FulfillingStoreMeta import FulfillingStoreMeta

































from .FulfillingStoreStoreAddressJson import FulfillingStoreStoreAddressJson








class PlatformFulfillingStore(BaseSchema):
    # Order swagger.json

    
    packaging_material_count = fields.Int(required=False)
    
    location_type = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    meta = fields.Nested(FulfillingStoreMeta, required=False)
    
    name = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    address1 = fields.Str(required=False)
    
    store_email = fields.Str(required=False)
    
    is_archived = fields.Boolean(required=False)
    
    state = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    contact_person = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    is_enabled_for_recon = fields.Boolean(required=False)
    
    fulfillment_channel = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    id = fields.Int(required=False)
    
    pincode = fields.Str(required=False)
    
    brand_store_tags = fields.List(fields.Str(required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    store_address_json = fields.Nested(FulfillingStoreStoreAddressJson, required=False)
    
    updated_at = fields.Str(required=False)
    
    login_username = fields.Str(required=False)
    
    country = fields.Str(required=False)
    

