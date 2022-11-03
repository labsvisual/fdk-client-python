"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .Media import Media




class Department(BaseSchema):
    # Catalog swagger.json

    
    priority_order = fields.Int(required=False)
    
    slug = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    name = fields.Str(required=False)
    

