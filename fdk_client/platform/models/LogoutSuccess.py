"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class LogoutSuccess(BaseSchema):
    # User swagger.json

    
    logout = fields.Boolean(required=False)
    

