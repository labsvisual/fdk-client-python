"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema























from .LocationDefaultCurrency import LocationDefaultCurrency

from .LocationDefaultLanguage import LocationDefaultLanguage


class LocationCountry(BaseSchema):
    # Common swagger.json

    
    capital = fields.Str(required=False)
    
    currency = fields.Str(required=False)
    
    iso2 = fields.Str(required=False)
    
    iso3 = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    parent = fields.Str(required=False)
    
    phone_code = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    uid = fields.Int(required=False)
    
    __v = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    default_currency = fields.Nested(LocationDefaultCurrency, required=False)
    
    default_language = fields.Nested(LocationDefaultLanguage, required=False)
    

