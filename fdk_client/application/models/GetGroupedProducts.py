"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .Products import Products
















class GetGroupedProducts(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    choice = fields.Str(required=False)
    
    products = fields.List(fields.Nested(Products, required=False), required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    active = fields.Boolean(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    

