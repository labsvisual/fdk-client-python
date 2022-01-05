"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



















from .BagItemAttributes import BagItemAttributes














class BagItem(BaseSchema):
    # Order swagger.json

    
    id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    slug_key = fields.Str(required=False)
    
    can_return = fields.Boolean(required=False)
    
    brand_id = fields.Int(required=False)
    
    l2_category = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    
    can_cancel = fields.Boolean(required=False)
    
    attributes = fields.Nested(BagItemAttributes, required=False)
    
    l3_category_name = fields.Str(required=False)
    
    l3_category = fields.Int(required=False)
    
    l1_category = fields.List(fields.Str(required=False), required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    brand = fields.Str(required=False)
    
    last_updated_at = fields.Str(required=False)
    

