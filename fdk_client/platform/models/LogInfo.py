"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class LogInfo(BaseSchema):
    # Analytics swagger.json

    
    _id = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    event_type = fields.Str(required=False)
    
    marketplace_name = fields.Str(required=False)
    
    event = fields.Str(required=False)
    
    trace_id = fields.Str(required=False)
    
    company_id = fields.Float(required=False)
    
    brand_id = fields.Float(required=False)
    
    store_code = fields.Str(required=False)
    
    store_id = fields.Float(required=False)
    
    item_id = fields.Float(required=False)
    
    article_id = fields.Str(required=False)
    
    seller_identifier = fields.Str(required=False)
    

