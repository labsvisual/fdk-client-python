"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductBulkAssets(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    url = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    

