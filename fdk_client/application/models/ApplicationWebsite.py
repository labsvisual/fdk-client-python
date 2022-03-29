"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class ApplicationWebsite(BaseSchema):
    # Common swagger.json

    
    enabled = fields.Boolean(required=False)
    
    basepath = fields.Str(required=False)
    

