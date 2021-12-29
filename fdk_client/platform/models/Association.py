"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class Association(BaseSchema):
    # Webhook swagger.json

    
    company_id = fields.Int(required=False)
    
    application_id = fields.List(fields.Str(required=False), required=False)
    
    extension_id = fields.Str(required=False)
    
    criteria = fields.Str(required=False)
    

