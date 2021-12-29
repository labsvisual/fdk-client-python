"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class AuthSuccessUserEmails(BaseSchema):
    # User swagger.json

    
    email = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    active = fields.Boolean(required=False)
    

