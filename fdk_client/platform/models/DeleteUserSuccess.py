"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class DeleteUserSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    

