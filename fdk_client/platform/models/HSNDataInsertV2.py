"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .TaxSlab import TaxSlab












class HSNDataInsertV2(BaseSchema):
    # Catalog swagger.json

    
    hsn_code = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    modified_by = fields.Dict(required=False)
    
    description = fields.Str(required=False)
    
    taxes = fields.List(fields.Nested(TaxSlab, required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    reporting_hsn = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    created_by = fields.Dict(required=False)
    

