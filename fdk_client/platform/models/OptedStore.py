"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .OptedStoreAddress import OptedStoreAddress








class OptedStore(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    address = fields.Nested(OptedStoreAddress, required=False)
    
    display_name = fields.Str(required=False)
    
    store_type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

