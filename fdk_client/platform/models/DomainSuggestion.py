"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class DomainSuggestion(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    unsupported = fields.Boolean(required=False)
    
    is_available = fields.Boolean(required=False)
    
    price = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    

