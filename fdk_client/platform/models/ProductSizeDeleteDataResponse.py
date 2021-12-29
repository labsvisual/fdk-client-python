"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ProductSizeDeleteDataResponse(BaseSchema):
    # Catalog swagger.json

    
    size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    

