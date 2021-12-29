"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema













from .ContactSchema import ContactSchema


class Support(BaseSchema):
    # Content swagger.json

    
    created = fields.Boolean(required=False)
    
    _id = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    contact = fields.Nested(ContactSchema, required=False)
    

