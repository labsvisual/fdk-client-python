"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class TokenRequestBodySchema(BaseSchema):
    # User swagger.json

    
    token = fields.Str(required=False)
    

