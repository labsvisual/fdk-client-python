"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class HasPasswordSuccess(BaseSchema):
    # User swagger.json

    
    result = fields.Boolean(required=False)
    

