"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class CrossSellingData(BaseSchema):
    # Catalog swagger.json

    
    products = fields.Int(required=False)
    
    articles = fields.Int(required=False)
    

