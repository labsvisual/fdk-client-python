"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class TaxIdentifier(BaseSchema):
    # Catalog swagger.json

    
    reporting_hsn = fields.Str(required=False)
    
    hsn_code = fields.Str(required=False)
    
    hsn_code_id = fields.Str(required=False)
    

