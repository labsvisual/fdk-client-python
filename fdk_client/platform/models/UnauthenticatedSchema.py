"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class UnauthenticatedSchema(BaseSchema):
    # User swagger.json

    
    authenticated = fields.Boolean(required=False)
    

