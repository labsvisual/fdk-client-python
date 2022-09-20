"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductBulkAssets(BaseSchema):
    # Catalog swagger.json

    
    url = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    user = fields.Dict(required=False)
    

