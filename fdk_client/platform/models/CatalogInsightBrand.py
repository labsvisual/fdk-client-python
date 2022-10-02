"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CatalogInsightBrand(BaseSchema):
    # Catalog swagger.json

    
    total_sizes = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    total_articles = fields.Int(required=False)
    
    article_freshness = fields.Int(required=False)
    
    available_articles = fields.Int(required=False)
    

