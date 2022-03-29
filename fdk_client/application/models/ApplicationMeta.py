"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ApplicationMeta(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

