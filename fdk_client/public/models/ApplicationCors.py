"""Public Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




class ApplicationCors(BaseSchema):
    # Configuration swagger.json

    
    domains = fields.List(fields.Str(required=False), required=False)
    

