"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema








class ItemQuery(BaseSchema):
    # Catalog swagger.json

    
    brand_uid = fields.Int(required=False)
    
    uid = fields.Int(required=False)
    
    item_code = fields.Str(required=False)
    

