"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema


















class Identifier(BaseSchema):
    # Cart swagger.json

    
    collection_id = fields.List(fields.Str(required=False), required=False)
    
    user_id = fields.List(fields.Str(required=False), required=False)
    
    brand_id = fields.List(fields.Int(required=False), required=False)
    
    category_id = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.List(fields.Int(required=False), required=False)
    
    company_id = fields.List(fields.Int(required=False), required=False)
    
    store_id = fields.List(fields.Int(required=False), required=False)
    
    article_id = fields.List(fields.Str(required=False), required=False)
    

