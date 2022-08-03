"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PageResponseType(BaseSchema):
    # Catalog swagger.json

    
    current = fields.Int(required=False)
    
    next = fields.Int(required=False)
    
    has_next = fields.Boolean(required=False)
    
    total_count = fields.Int(required=False)
    

