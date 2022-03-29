"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ApplicationAuth(BaseSchema):
    # Common swagger.json

    
    enabled = fields.Boolean(required=False)
    

