"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Domain import Domain

from .ApplicationWebsite import ApplicationWebsite

from .ApplicationCors import ApplicationCors





from .ApplicationMeta import ApplicationMeta







from .SecureUrl import SecureUrl

from .SecureUrl import SecureUrl




class ApplicationInfo(BaseSchema):
    # Configuration swagger.json

    
    _id = fields.Str(required=False)
    
    domain = fields.Nested(Domain, required=False)
    
    website = fields.Nested(ApplicationWebsite, required=False)
    
    cors = fields.Nested(ApplicationCors, required=False)
    
    description = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    meta = fields.Nested(ApplicationMeta, required=False)
    
    token = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    banner = fields.Nested(SecureUrl, required=False)
    
    logo = fields.Nested(SecureUrl, required=False)
    
    is_active = fields.Boolean(required=False)
    

