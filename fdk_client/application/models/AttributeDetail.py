"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class AttributeDetail(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    logo = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    key = fields.Str(required=False)
    

