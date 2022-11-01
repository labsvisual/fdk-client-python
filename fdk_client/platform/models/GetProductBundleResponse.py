"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .GetProducts import GetProducts














class GetProductBundleResponse(BaseSchema):
    # Catalog swagger.json

    
    meta = fields.Dict(required=False)
    
    choice = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    products = fields.List(fields.Nested(GetProducts, required=False), required=False)
    
    logo = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    

