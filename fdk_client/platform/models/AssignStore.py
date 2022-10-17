"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .AssignStoreArticle import AssignStoreArticle








class AssignStore(BaseSchema):
    # Catalog swagger.json

    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    pincode = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    articles = fields.List(fields.Nested(AssignStoreArticle, required=False), required=False)
    
    app_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    channel_identifier = fields.Str(required=False)
    

