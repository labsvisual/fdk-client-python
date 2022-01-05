"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .SecureUrl import SecureUrl

from .SecureUrl import SecureUrl

from .SecureUrl import SecureUrl

from .SecureUrl import SecureUrl

from .Domain import Domain

from .Domain import Domain




class ApplicationDetail(BaseSchema):
    # Configuration swagger.json

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    mobile_logo = fields.Nested(SecureUrl, required=False)
    
    favicon = fields.Nested(SecureUrl, required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    domain = fields.Nested(Domain, required=False)
    
    domains = fields.List(fields.Nested(Domain, required=False), required=False)
    
    _id = fields.Str(required=False)
    

