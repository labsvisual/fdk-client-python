"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema





from .AuthSuccessUserDebug import AuthSuccessUserDebug



from .AuthSuccessUserEmails import AuthSuccessUserEmails


class AuthSuccessUser(BaseSchema):
    # User swagger.json

    
    first_name = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    debug = fields.Nested(AuthSuccessUserDebug, required=False)
    
    active = fields.Boolean(required=False)
    
    emails = fields.Nested(AuthSuccessUserEmails, required=False)
    

