"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .DefaultCurrency import DefaultCurrency






class AppSupportedCurrency(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    supported_currency = fields.List(fields.Str(required=False), required=False)
    
    application = fields.Str(required=False)
    
    default_currency = fields.Nested(DefaultCurrency, required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    

