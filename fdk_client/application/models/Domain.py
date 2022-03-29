"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class Domain(BaseSchema):
    # Common swagger.json

    
    verified = fields.Boolean(required=False)
    
    is_primary = fields.Boolean(required=False)
    
    is_shortlink = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    

