"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .ApplicationAuth import ApplicationAuth






class App(BaseSchema):
    # Configuration swagger.json

    
    company_id = fields.Str(required=False)
    
    channel_type = fields.Str(required=False)
    
    auth = fields.Nested(ApplicationAuth, required=False)
    
    name = fields.Str(required=False)
    
    desc = fields.Str(required=False)
    

